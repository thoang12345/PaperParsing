from __future__ import annotations
from pathlib import Path
import zipfile
from bs4 import BeautifulSoup
from Functions import functionsClassify as pdfFun
from dataclasses import dataclass, field
from enum import Enum
from typing import Any
import torch
import time
import subprocess
import shutil
import re
import logging
from pytictoc import TicToc
import os

#docling bullshiiiiittt
from docling.datamodel.accelerator_options import (
    AcceleratorDevice,
    AcceleratorOptions,
)
from docling.datamodel.pipeline_options import (
    EasyOcrOptions,
    RapidOcrOptions,
    LayoutOptions,
    TableFormerMode,
    TableStructureOptions,
    ThreadedPdfPipelineOptions,
)

from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.layout_model_specs import DOCLING_LAYOUT_EGRET_LARGE
from docling_core.types.doc import ImageRefMode

#docling chunking bullshitttttt
from docling.chunking import HybridChunker
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer
from transformers import AutoTokenizer

#chromaDB stuff
import chromadb

#system objects
logging.basicConfig(level=logging.INFO,
                     format='%(asctime)s - %(levelname)s - %(message)s',
                     datefmt='%Y-%m-%d %I:%M:%S %p')
logger = logging.getLogger(__name__)

t = TicToc()

def giveGPUstatus() -> None:
        logger.info("=" * 50)
        logger.info(f"torch: {torch.__version__}")
        logger.info(f"hip: {torch.version.hip}")
        logger.info(f"cuda available: {torch.cuda.is_available()}")

        if not torch.cuda.is_available():
                raise SystemExit("ROCm GPU is not visible to PyTorch")

        device = "cuda"
        logger.info(f"device: {torch.cuda.get_device_name(0)}")

        x = torch.randn((4096, 4096), device=device, dtype=torch.float16)
        y = torch.randn((4096, 4096), device=device, dtype=torch.float16)

        torch.cuda.synchronize()
        start = time.time()

        for _ in range(20):
                z = x @ y

        torch.cuda.synchronize()
        logger.info(f"seconds: {round(time.time() - start, 3)}")
        logger.info(f"ok: {z.shape}, {z.dtype}")
        logger.info(f"{'=' * 50}\n")

def buildRelativePaths(paths : list[str]) -> list[Path]:
        relativePath = Path(__file__).parent.parent
        buildRelativePaths = [relativePath / path for path in paths]
        
        return buildRelativePaths

def parseFiles(path : Path) -> list[str]:
        fileNames = [file.name for file in path.iterdir() if file.is_file() and "Zone.Identifier" not in file.name]
        
        return fileNames

def filterPDFs(path : Path) -> list[str]:
        files = parseFiles(path)
        PDFFiles = [pdf for pdf in files if pdf.endswith(".pdf")]
        
        return PDFFiles

def separatePDFs(path : Path) -> tuple[list[Path], list[Path]]:
        files = parseFiles(path)
        pdfs = filterPDFs(path)
        not_pdfs = [pdf for pdf in files if not pdf.endswith((".pdf", ".doc", ".ppt", ".xls"))]
        
        return pdfs, not_pdfs

def classifyPDFs(path : Path) -> list[dict[str : str, str : str, str : str]]:
        pdfs, not_pdfs = separatePDFs(path)
        pageData = pdfFun.extractPageData(path, pdfs)
        classifications = pdfFun.PDFclassifier(pageData)

        return classifications     

def classifyEverythingElse(path : Path) -> list[dict[str : str, str : str, str : str]]:
        pdfs, notPDFS = separatePDFs(path)
        classificatiions = generalClassifier(path, notPDFS)
        
        return classificatiions

def generalClassifier(path: Path, files: list[str]) -> list[dict[str, str]]:
        pageData = []
         
        for file in files:
                filePath = path / file
                fileExtension = Path(file).suffix.lower().lstrip(".")
                
                if fileExtension in ["docx", "pptx", "xlsx"]:
                        with zipfile.ZipFile(filePath, "r") as microsoftSuiteFile:
                                names = microsoftSuiteFile.namelist()

                                has_media = any(
                                name.startswith("word/media/") or
                                name.startswith("ppt/media/") or
                                name.startswith("xl/media/")
                                for name in names
                                )

                        pageData.append({
                                "file": file,
                                "file_type": fileExtension,
                                "text_type": "generalFile",
                                "content_type": "mixedFile" if has_media else "nativeFile"
                        })

                elif fileExtension in ["html", "htm", "xhtml", "xml"]:
                        content = filePath.read_text(encoding="utf-8", errors="ignore")

                        if fileExtension in ["html", "htm"]:
                                parsedContent = BeautifulSoup(content, "html.parser")
                                has_media = parsedContent.find("img") is not None
                        else:
                                parsedContent = BeautifulSoup(content, "xml")
                                has_media = parsedContent.find(["img", "image"]) is not None

                        pageData.append({
                                "file": file,
                                "file_type": fileExtension,
                                "text_type": "generalFile",
                                "content_type": "mixedFile" if has_media else "nativeFile"
                        })

                else:
                        pageData.append({
                                "file": file,
                                "file_type": fileExtension,
                                "text_type": "generalFile",
                                "content_type": "nativeFile"
                        })
        return pageData

def printFilesAndConfigurations(pdfClassification : list[dict[str : str, str : str, str : str]], not_pdfs : list[dict[str : str, str : str, str : str]]) -> None:
        allClassifications = [{"classification_group": "PDF",**pdf}
        for pdf in pdfClassification
        ] + [
        {
        "classification_group": "General",
        **general
        }
        for general in not_pdfs
        ]

        lines = [
        "=" * 50,
        f"File Classifications: {len(allClassifications)} total",
        f"PDF Classifications: {len(pdfClassification)}",
        f"General Classifications: {len(not_pdfs)}",
        "=" * 50,
        ]

        for index, item in enumerate(allClassifications, start=1):
                lines.append(
                f"{index:02d}. "
                f"[{item['classification_group']}] "
                f"{item['file']} | "
                f"type={item['file_type']} | "
                f"text={item['text_type']} | "
                f"content={item['content_type']}"
                )

        lines.append("=" * 50)

        logger.info("\n%s", "\n".join(lines))

def chooseParserPlan(pdfClassification : list[dict[str : str, str : str, str : str]], not_pdfs : list[dict[str : str, str : str, str : str]]) -> list[dict[str, str]]:
        parserPlans = []
        
        for pdf in pdfClassification:
                if pdf["content_type"] == "scientific" and (pdf["text_type"] == "scannedPDF" or pdf["text_type"] == "nativePDF"):
                        pdf["parser_plan"] = "markerOCR"

                if pdf["content_type"] == "scientific" and pdf["text_type"] == "mixedPDF":
                        pdf["parser_plan"] = "markerOCRPlusLLM"

                if pdf["content_type"] == "generic" and pdf["text_type"] == "mixedPDF":
                        pdf["parser_plan"] = "doclingOCR"

                if pdf["content_type"] == "generic" and pdf["text_type"] == "scannedPDF":
                        pdf["parser_plan"] = "doclingScannedOCR"
                
                if pdf["content_type"] == "generic" and pdf["text_type"] == "nativePDF":
                        pdf["parser_plan"] = "doclingNative"

                if pdf["content_type"] == "generic" and pdf["text_type"] == "unknown":
                        pdf["parser_plan"] = "doclingNative"

                parserPlans.append(pdf)
        
        for notPDF in not_pdfs:
                if notPDF["content_type"] == "mixedFile":
                        notPDF["parser_plan"] = "doclingOCR"
                
                if notPDF["content_type"] == "nativeFile":
                        notPDF["parser_plan"] = "doclingNative"
                
                parserPlans.append(notPDF)

        return parserPlans

class profileNames(str, Enum):
        doclingOCR = "doclingOCR"
        doclingScannedOCR = "doclingScannedOCR"
        doclingNative = "doclingNative"
        markerOCR = "markerOCR"
        markerOCRPlusLLM = "markerOCRPlusLLM"

@dataclass(frozen=True)
class doclingPipelineOptions:
        name: profileNames

        #image / visual assets 
        imageScale : float = 1.0
        generatePictureImages : bool = False
        generatePageImage : bool = False
        
        #bum ahh OCR
        doOCR : bool = False
        forceFullPageOCR : bool = False
        ocrBatchSize : int = 4
        ocrEngine : str = "easyocr"

        #layout
        layoutBatchSize : int = 4
        useEgretLargeLayout : bool = False

        #tables
        doTableStructures : bool = False
        tableDoCellMatching : bool = False
        tableAccurateMode : bool = False
        tableBatchSize : int = 4

        #enrichments
        doFormulaEnrichment : bool = False
        doPictureDescriptions : bool = False
        pictureDescriptionPrompt : str = None

        #Hardware/Threading
        acceleratorDevice : str = "auto"
        numberOfThreads : int = 4

        #safety/plugins
        allowExternalPlugins : bool = True

doclingProfiles: dict[profileNames, doclingPipelineOptions] = {
        profileNames.doclingNative: doclingPipelineOptions(
                name = profileNames.doclingNative,
                doOCR = False,
                doTableStructures=True,
                tableAccurateMode=False,
                generatePageImage=False,
                generatePictureImages=False,
                doFormulaEnrichment=True,
                doPictureDescriptions=False,
                imageScale=1.0
        ),

        profileNames.doclingScannedOCR : doclingPipelineOptions(
                name=profileNames.doclingScannedOCR,
                doOCR=True,
                forceFullPageOCR=True,
                ocrEngine="rapidocr",
                ocrBatchSize=1,
                layoutBatchSize=1,
                doTableStructures=True,
                tableAccurateMode=True,
                generatePageImage=False,
                generatePictureImages=True,
                useEgretLargeLayout=True,
                imageScale=1.1,
                numberOfThreads=2
        ),

        profileNames.doclingOCR : doclingPipelineOptions(
                name=profileNames.doclingOCR,
                doOCR=True,
                forceFullPageOCR=False,
                doTableStructures=True,
                tableAccurateMode=True,
                generatePictureImages=True,
                generatePageImage=False,
                useEgretLargeLayout=True,
                imageScale=1.25
        )
}

def doclingSettings(profile : doclingPipelineOptions) -> ThreadedPdfPipelineOptions:
        options = ThreadedPdfPipelineOptions()

        # Images
        options.images_scale = profile.imageScale
        options.generate_picture_images = profile.generatePictureImages
        options.generate_page_images = profile.generatePageImage

        # OCR
        options.do_ocr = profile.doOCR
        options.ocr_batch_size = profile.ocrBatchSize
        if profile.ocrEngine == "rapidocr":
                options.ocr_options = RapidOcrOptions(
                        backend="torch",
                        lang=["english"],
                        force_full_page_ocr=profile.forceFullPageOCR,
                        print_verbose=False,
        )
        else:
                options.ocr_options = EasyOcrOptions(
                        force_full_page_ocr=profile.forceFullPageOCR
                )

        # Layout
        options.layout_batch_size = profile.layoutBatchSize
        if profile.useEgretLargeLayout:
                options.layout_options = LayoutOptions(
                model_spec=DOCLING_LAYOUT_EGRET_LARGE
                )

        # Tables
        options.do_table_structure = profile.doTableStructures
        options.table_batch_size = profile.tableBatchSize
        options.table_structure_options = TableStructureOptions(
                do_cell_matching=profile.tableDoCellMatching,
                mode=(
                TableFormerMode.ACCURATE
                if profile.tableAccurateMode
                else TableFormerMode.FAST
                ),
        )

        # Enrichments
        options.do_formula_enrichment = profile.doFormulaEnrichment
        options.do_picture_description = profile.doPictureDescriptions

        if profile.doPictureDescriptions:
                options.picture_description_options.prompt = profile.pictureDescriptionPrompt

        # Hardware
        options.accelerator_options = AcceleratorOptions(
                num_threads=profile.numberOfThreads,
                device=AcceleratorDevice(profile.acceleratorDevice),
        )

        # Plugins
        options.allow_external_plugins = profile.allowExternalPlugins

        return options

@dataclass(frozen=True)
class markerPipelineOptions:
        name: profileNames

        outputFormat: list[str] = field(default_factory=lambda: ["markdown", "json"])
        pageRanges: str | None = None
        forceOCR: bool = False
        paginateOutput: bool = False
        useLLM: bool = False
        workers: int = 1
        stripExistingOCR: bool = False
        llmServices: str = ""
        redoInlineMath: bool = False

markerProfiles: dict[profileNames, markerPipelineOptions] = {
        profileNames.markerOCR: markerPipelineOptions(
                name=profileNames.markerOCR,
                forceOCR=False,
                paginateOutput=True,
                workers=8,
                stripExistingOCR=True,
                useLLM=False,
        ),

        profileNames.markerOCRPlusLLM: markerPipelineOptions(
                name=profileNames.markerOCR,
                forceOCR=False,
                paginateOutput=True,
                workers=8,
                stripExistingOCR=True,
                useLLM=True
        )
}

def runMarkerCLI(batch: list[dict[str, str]], inputFolder: Path, outputFolder: Path, profile : markerPipelineOptions, parserName: str, batchNumber : int, outputFormat: str) -> dict[str, Any]:
        stageDirectory = outputFolder / "_markerStage" / parserName / f"batch_{batchNumber:03d}"
        resultDirectory = outputFolder / "marker" / parserName / outputFormat
        
        if stageDirectory.exists():
                shutil.rmtree(stageDirectory)

        resultDirectory.mkdir(parents=True, exist_ok=True)
        stageDirectory.mkdir(parents=True, exist_ok=True)

        for file in batch:
               sourcePath = inputFolder / file["file"]
               destinationPath = stageDirectory / file["file"]
               shutil.copy2(sourcePath, destinationPath)

        command = [
                "marker", str(stageDirectory),
                "--output_dir", str(resultDirectory),
                "--output_format", outputFormat,
                "--workers", str(profile.workers)
                ]
        
        if profile.forceOCR:
               command.append("--force_ocr")
        if profile.paginateOutput:
               command.append("--paginate_output")
        if profile.useLLM:
               command.append("--use_llm")
        if profile.pageRanges is not None:
               command.extend(["--page_ranges", profile.pageRanges])
        if profile.stripExistingOCR:
               command.append("--strip_existing_ocr")

        completed = subprocess.run(command, check=True)

        summary = {
               "parserName": parserName,
               "batchNumber": batchNumber,
               "outputFormat": outputFormat,
               "stageDirectory": stageDirectory,
               "outputDirectory": resultDirectory,
               "command": command,
               "returnCode": completed.returncode,
               "stdout": completed.stdout,
               "stderr": completed.stderr,
               "batch": batch
        }

        return summary

def convertPDFsMarker(pdfClassification : list[dict[str : str, str : str, str : str]], not_pdfs : list[dict[str : str, str : str, str : str]], inputFolder : Path, outputFolder : Path) -> list[dict[str, str]]:
        parserPlans = chooseParserPlan(pdfClassification, not_pdfs)
        sortedParserPlans = sorted(parserPlans, key=lambda x: x["parser_plan"])
        markerPlans = [item for item in sortedParserPlans if item["parser_plan"] == "markerOCR"]
        batches = batchParserPlans(markerPlans)
        batchPlans = addParserPlansSettings(batches)
        results = []
        
        for parserName, plan in batchPlans.items():
                settings = plan["settings"]
                batches = plan["batches"]

                for batchNumber, batch in enumerate(batches, start=1):
                       for outputFormat in settings.outputFormat:
                                result = runMarkerCLI(
                                        batch=batch,
                                        inputFolder=inputFolder,
                                        outputFolder=outputFolder,
                                        profile=settings,
                                        parserName=parserName,
                                        batchNumber=batchNumber,
                                        outputFormat=outputFormat,
                                )

                                results.append(result)

                                if result["returnCode"] != 0:
                                        raise RuntimeError(
                                                f"Marker failed for {parserName} batch {batchNumber} "
                                                f"with output format {outputFormat}\n\n"
                                                f"{result['stderr']}"
                                        )
        return results

def buildDoclingConverterSettings(profile : doclingPipelineOptions) -> DocumentConverter:
        return DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(
                    pipeline_options=doclingSettings(profile)
                )
            }
        )

def convertDocumentsDocling(pdfClassification : list[dict[str : str, str : str, str : str]], not_pdfs : list[dict[str : str, str : str, str : str]], inputFolder : Path, outputFolder : Path, chunkingTools : list[HybridChunker, HuggingFaceTokenizer]) -> list[dict[str, Any]]:
        parserPlans = chooseParserPlan(pdfClassification, not_pdfs)
        sortedParserPlans = sorted(parserPlans, key=lambda x: x["parser_plan"])
        batches = batchParserPlans(sortedParserPlans)
        batches.pop("markerOCR", None)
        batchPlans = addParserPlansSettings(batches)
        results = []

        for parserName, plan in batchPlans.items():
                logger.info(f"Converting {parserName} plans")

                profile = plan["profile"]
                converter = plan["settings"]

                for batch in plan["batches"]:
                        files = [
                        inputFolder / item["file"]
                        for item in batch
                        ]

                        logger.info(f"{parserName}: {[item.name for item in files]}")

                        convertedFile = converter.convert_all(files)

                        results.append({
                        "name": parserName,
                        "profile": profile,
                        "settings": converter,
                        "result": convertedFile,
                        "batch": batch,
                        })

        exportResults(results, outputFolder, chunkingTools)

        return results

def addParserPlansSettings(batchParserPlans : dict[str, list[list[dict[str, Any]]]]) -> dict[str, dict[str, Any]]:
    parserPlansWithSettings = {}

    for parserName, parserBatches in batchParserPlans.items():
        if parserName == "doclingOCR":
            settings = buildDoclingConverterSettings(doclingProfiles[profileNames.doclingOCR])
            profile = doclingProfiles[profileNames.doclingOCR]

        elif parserName == "doclingScannedOCR":
            settings = buildDoclingConverterSettings(doclingProfiles[profileNames.doclingScannedOCR])
            profile = doclingProfiles[profileNames.doclingScannedOCR]

        elif parserName == "doclingNative":
            settings = buildDoclingConverterSettings(doclingProfiles[profileNames.doclingNative])
            profile = doclingProfiles[profileNames.doclingNative]

        elif parserName == "markerOCR":
            settings = markerProfiles[profileNames.markerOCR]
            profile = buildDoclingConverterSettings

        elif parserName == "markerOCRPlusLLM":
                settings = markerProfiles[profileNames.markerOCRPlusLLM]
                profile = buildDoclingConverterSettings

        else:
            continue

        parserPlansWithSettings[parserName] = {
            "settings": settings,
            "profile": profile,
            "batches": parserBatches
        }

    return parserPlansWithSettings

def batchParserPlans(parserPlans : list[dict[str, str]]) -> dict[str, list[list[dict[str, Any]]]]:
        batches = {}
        batchSizes = {
                "doclingScannedOCR": 1,
                "doclingOCR": 2,
                "doclingNative": 8,
                "markerOCR": 12,
        }
        
        for item in parserPlans:
                parser = item["parser_plan"]
                parserBatchSize = batchSizes.get(parser, 1)

                parser_batches = batches.setdefault(parser, [])

                if not parser_batches or len(parser_batches[-1]) >= parserBatchSize:
                        parser_batches.append([])

                parser_batches[-1].append(item)

        return batches

def doclingMarkdownUsesImages(profile: doclingPipelineOptions) -> bool:
        return bool(profile.generatePictureImages or profile.generatePageImage)

def exportResults(results: list[dict[str, Any]], outputFolder: Path) -> None:
        for parser_result in results:
                parserName = parser_result["name"]
                profile = parser_result["profile"]
                conversionGenerator = parser_result["result"]
                batch = parser_result["batch"]

                markdownOutput = outputFolder / "docling" / parserName / "markdown"
                jsonOutput = outputFolder / "docling" / parserName / "json"
                assetOutput = outputFolder / "docling" / parserName / "assets"

                markdownOutput.mkdir(parents=True, exist_ok=True)
                jsonOutput.mkdir(parents=True, exist_ok=True)
                assetOutput.mkdir(parents=True, exist_ok=True)   

                useImageLinks = doclingMarkdownUsesImages(profile)
        
                logger.info(f"\nResults from {parserName}")
                logger.info(f"Profile: {profile.name}")
                logger.info(f"Image links enabled: {useImageLinks}\n")

                for item, conversionResult in zip(batch, conversionGenerator):
                        document = conversionResult.document

                        if document is None:
                                logger.info(f"Skipping failed conversion: {item['file']}")
                                continue

                        sourceName = item["file"]
                        stem = Path(sourceName).stem

                        markdownDir = markdownOutput / stem
                        jsonDir = jsonOutput / stem
                        artifactDir = assetOutput / stem

                        markdownDir.mkdir(parents=True, exist_ok=True)
                        jsonDir.mkdir(parents=True, exist_ok=True)
                        artifactDir.mkdir(parents=True, exist_ok=True)

                        markdownPath = markdownDir / f"{stem}.md"
                        jsonPath = jsonDir / f"{stem}.json"

                        if useImageLinks:
                                document.save_as_markdown(
                                markdownPath,
                                artifacts_dir=artifactDir,
                                image_mode=ImageRefMode.REFERENCED,
                                page_break_placeholder="----page-break-here----"
                                )
                        else:
                                document.save_as_markdown(
                                markdownPath,
                                artifacts_dir=artifactDir,
                                image_mode=ImageRefMode.PLACEHOLDER,
                                page_break_placeholder="----page-break-here----"
                                )

                        document.save_as_json(
                                jsonPath,
                                image_mode=ImageRefMode.PLACEHOLDER
                        )

                        logger.info(f"Generated markdown: {markdownPath} for {item['file']}")

def initializeDoclingChunker() -> list[HybridChunker, HuggingFaceTokenizer]:
        EMBED_MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
        MAX_TOKENS = 400

        logger.info("=" * 50)
        logger.info(f"Initializing Docling Chunker with model: {EMBED_MODEL_ID} and max tokens: {MAX_TOKENS}")
        tokenizer = HuggingFaceTokenizer(
                tokenizer = AutoTokenizer.from_pretrained(EMBED_MODEL_ID),
                max_tokens = MAX_TOKENS
        )

        logger.info(f"Initializing HybridChunker with tokenizer and merge_peers set to True")
        logger.info("=" * 50 + "\n")
        chunker = HybridChunker(
                tokenizer=tokenizer,
                merge_peers = True
        )

        chunkingTools = [chunker, tokenizer]
        return chunkingTools

def createChromaDBClient(chromaDBFolder: Path) -> chromadb.api.client.Client:
        client = chromadb.PersistentClient(path=str(chromaDBFolder))
        return client

def createOrDeleteChromaDBCollection(client: chromadb.api.client.Client) -> None:
        answer: str = ""

        while answer.lower() != "n":
                collections = getChromaDBCollections(client)

                if collections == []:
                        answer = input("\nNo existing collections found. Would you like to create a new collection? (y/n): ")
                else: 
                        answer = input("\nExisting collections found. Would you like to create a new collection? (y/n). Or 'd' to delete an existing collection: ")

                if answer.lower() == "d":
                        deleteChromaDBCollection(client)

                if answer.lower() == "y":
                        createChromaDBCollection(client)

def getChromaDBCollections(client: chromadb.api.client.Client) -> chromadb.api.models.Collection:
        collections = client.list_collections()
        return collections

def deleteChromaDBCollection(client: chromadb.api.client.Client) -> None:
        collections = getChromaDBCollections(client)
        collectionNames = [col.name for col in collections]
        logger.info(f"Existing collections: {', '.join(collectionNames)}")

        while True:
                collectionToDelete = input("Enter the name of the collection you want to delete. Or 'q' to quit: ")

                if collectionToDelete == 'q':
                        break
                if collectionToDelete in collectionNames:
                        client.delete_collection(name=collectionToDelete)
                        logger.info(f"Collection '{collectionToDelete}' deleted successfully.")
                else:
                        logger.info(f"Collection '{collectionToDelete}' not found.")
                        continue

def createChromaDBCollection(client: chromadb.api.client.Client) -> None:
        collections = []

        while True:
                collectionName = input("Enter the name for the new collection or 'q' to quit: ")
        
                if collectionName == 'q':
                        break
                if collectionName.strip() == "":
                        logger.info("Collection name cannot be empty. Please try again.")
                        continue
                
                collectionDescription = input("Enter a description for the new collection (optional): ")
                collections = client.create_collection(
                                        name=collectionName,
                                        metadata={"description": collectionDescription, "hnsw:space": "cosine"},
                                        configuration = {
                                                "hnsw": {
                                                        "space": "cosine",
                                                        "ef_construction": 1000,
                                                        "ef_search": 1000,
                                                        "max_neighbors": 64,
                                                        "num_threads": os.cpu_count(),
                                                        "batch_size": 100,
                                                        "sync_threshold": 1000,
                                                        "resize_factor": 1.2,
                                                }
                                        }
                                )
                logger.info(f"Collection '{collectionName}' created successfully.")

def addToChromaDB(client: chromadb.api.client.Client) -> None:
        collections = getChromaDBCollections(client)
        collectionNames = [col.name for col in collections]
        
        

        while True:
                answer = input(f"\nDo you want to add documents to an existing collection? (y/n): ").lower()
                
                if answer not in ["y", "n"]:
                        logger.info("Invalid answer, either 'y' or 'n'")
                        continue
                elif answer == "n":
                        break

                answer = input(f"\nSelect a collection from existing ones to add documents to: {', '.join(collectionNames)}. Or 'q' to quit: ")

                if answer == 'q':
                        break
                if answer.strip() == "":
                        logger.info("Input cannot be empty. Please try again.")
                        continue
                if answer not in collectionNames:
                        logger.info(f"Collection '{answer}' not found. Please try again.")
                        continue
                if answer in collectionNames:
                        collection = client.get_collection(name=answer)
                        logger.info(f"Successfully found collection '{collection.name}'. You can now add documents to this collection.")
                        fileInputPath = input("Enter the path to the file you want to add to the collection: ")

                        if Path(fileInputPath).exists() and Path(fileInputPath).is_file():
                                collection = client.get_collection(name=answer)
                                logger.info(f"Successfully found file '{Path(fileInputPath).name}'. Adding chunks to collection '{collection.name}'...")

                                with open(fileInputPath, "r", encoding="utf-8") as file:
                                        content = file.read()
                                        logger.info(f"Splitting {Path(fileInputPath).name} into chunks...")
                                        
                                        pattern = r"===\s*\d+\s*==="
                                        chunks = re.split(pattern, content)
                                        chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

                                        logger.info(f"Adding {len(chunks)} chunks to collection '{collection.name}'...")
                                        for i, chunk in enumerate(chunks, start=1):
                                                collection.add(
                                                        documents=[chunk],
                                                        metadatas=[{"source": f"{Path(fileInputPath).name}_chunk_{i}"}],
                                                        ids=[f"{Path(fileInputPath).stem}_chunk_{i}"]
                                                )
                                                logger.info(f"Added chunk {i}/{len(chunks)} to collection '{collection.name}'.")
                                continue
                        else:
                                logger.info(f"Collection '{answer}' not found. Please try again.")
                                continue


def queryChromaDB(client: chromadb.api.client.Client) -> None:
        collections = getChromaDBCollections(client)
        collectionNames = [col.name for col in collections]

        while True:
                answer = input(f"\nDo you want to query an existing collection? (y/n): ").lower()

                if answer not in ["y", "n"]:
                        logger.info("Invalid answer, either 'y' or 'n'")
                        continue
                elif answer == "n":
                        break

                answer = input(f"\nSelect a collection from existing ones to query: {', '.join(collectionNames)}. Or 'q' to quit: ")

                if answer == 'q':
                        break
                if answer.strip() == "":
                        logger.info("Input cannot be empty. Please try again.")
                        continue
                if answer not in collectionNames:
                        logger.info(f"Collection '{answer}' not found. Please try again.")
                        continue
                if answer in collectionNames:
                        collection = client.get_collection(name=answer)
                        logger.info(f"Successfully found collection '{collection.name}'. You can now query this collection.")
                        while True:
                                queryInput = input("Enter your query or 'q' to quit: ")

                                if queryInput.strip() == "":
                                        logger.info("Query cannot be empty. Please try again.")
                                        continue
                                if queryInput == 'q':
                                        break

                                result = collection.query(
                                        query_texts=[queryInput],
                                        n_results=6
                                )
                                
                                for ids, documents, metadatas, distances in zip(result["ids"], result["documents"], result["metadatas"], result["distances"]):
                                        for id, document, metadata, distance in zip(ids, documents, metadatas, distances):
                                                logger.info(f"ID: {id}\nDistance: {distance}\nDocument: {document}\nMetadata: {metadata}\n{'-'*40}")
                                        print("\n")

                                        
def findOutputFiles(outputFolder: Path, pdfClassification : list[dict[str : str, str : str, str : str]], not_pdfs : list[dict[str : str, str : str, str : str]]) -> None:
        parserPlans = chooseParserPlan(pdfClassification, not_pdfs)
        sortedParserPlans = sorted(parserPlans, key=lambda x: x["parser_plan"])
        
        names = [Path(entry["file"]).stem for entry in sortedParserPlans]

        outputFiles = []

        for i, name in enumerate(names):
                sortedParserPlans[i]["output"] = findMarkdownJSON(outputFolder, name)

        return sortedParserPlans

def findMarkdownJSON(outputFolder : Path, name : str) -> Path:
        #path = [path for path in outputFolder.rglob("*") if path.is_file() and path.suffix.lower() in {".md", ".json"} and name.lower() in path.name.lower()]

        markdown_file = next(outputFolder.rglob(f"{name}.md"), None)
        json_file = next(outputFolder.rglob(f"{name}.json"), None)

        return {"markdown" : markdown_file, "JSON" : json_file}