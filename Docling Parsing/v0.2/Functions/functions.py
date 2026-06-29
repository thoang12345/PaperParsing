from __future__ import annotations
from pathlib import Path
import zipfile
from bs4 import BeautifulSoup
from Functions import functionsClassify as pdfFun
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Generator
import torch
import time
import subprocess
import shutil

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

def giveGPUstatus() -> None:
        print("=" * 50)
        print("torch:", torch.__version__)
        print("hip:", torch.version.hip)
        print("cuda available:", torch.cuda.is_available())

        if not torch.cuda.is_available():
                raise SystemExit("ROCm GPU is not visible to PyTorch")

        device = "cuda"
        print("device:", torch.cuda.get_device_name(0))

        x = torch.randn((4096, 4096), device=device, dtype=torch.float16)
        y = torch.randn((4096, 4096), device=device, dtype=torch.float16)

        torch.cuda.synchronize()
        start = time.time()

        for _ in range(20):
                z = x @ y

        torch.cuda.synchronize()
        print("seconds:", round(time.time() - start, 3))
        print("ok:", z.shape, z.dtype)
        print(f"{'=' * 50}\n")

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

def chooseParserPlan(pdfClassification : list[dict[str : str, str : str, str : str]], not_pdfs : list[dict[str : str, str : str, str : str]]) -> list[dict[str, str]]:
        parserPlans = []
        
        for pdf in pdfClassification:
                if pdf["content_type"] == "scientific" and (pdf["text_type"] == "mixedPDF" or pdf["text_type"] == "scannedPDF" or pdf["text_type"] == "nativePDF"):
                        pdf["parser_plan"] = "markerOCR"

                if pdf["content_type"] == "generic" and pdf["text_type"] == "mixedPDF":
                        pdf["parser_plan"] = "doclingOCR"

                if pdf["content_type"] == "generic" and pdf["text_type"] == "scannedPDF":
                        pdf["parser_plan"] = "doclingScannedOCR"
                
                if pdf["content_type"] == "generic" and pdf["text_type"] == "nativePDF":
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
                        print_verbose=True,
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

markerProfiles: dict[profileNames, markerPipelineOptions] = {
        profileNames.markerOCR: markerPipelineOptions(
                name=profileNames.markerOCR,
                forceOCR=True,
                paginateOutput=True,
                workers=7
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

def convertDocumentsDocling(pdfClassification : list[dict[str : str, str : str, str : str]], not_pdfs : list[dict[str : str, str : str, str : str]], inputFolder : Path, outputFolder : Path) -> list[dict[str, Any]]:
        parserPlans = chooseParserPlan(pdfClassification, not_pdfs)
        sortedParserPlans = sorted(parserPlans, key=lambda x: x["parser_plan"])
        batches = batchParserPlans(sortedParserPlans)
        batches.pop("markerOCR", None)
        batchPlans = addParserPlansSettings(batches)
        results = []

        for parserName, plan in batchPlans.items():
                print(f"Converting {parserName} plans")

                profile = plan["profile"]
                converter = plan["settings"]

                for batch in plan["batches"]:
                        files = [
                        inputFolder / item["file"]
                        for item in batch
                        ]

                        print(f"{parserName}: {[item.name for item in files]}")

                        convertedFile = converter.convert_all(files)

                        results.append({
                        "name": parserName,
                        "profile": profile,
                        "settings": converter,
                        "result": convertedFile,
                        "batch": batch,
                        })

                exportResults(results, outputFolder)


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

        
                print(f"\nResults from {parserName}")
                print(f"Profile: {profile.name}")
                print(f"Image links enabled: {useImageLinks}")

                for item, conversionResult in zip(batch, conversionGenerator):
                        document = conversionResult.document

                        if document is None:
                                print(f"Skipping failed conversion: {item['file']}")
                                continue
                        
                        sourceName = item["file"]
                        stem = Path(sourceName).stem

                        markdownPath = markdownOutput / f"{stem}.md"
                        jsonPath = jsonOutput / f"{stem}.json"
                        artifactDir = assetOutput / stem
                        artifactDir.mkdir(parents=True, exist_ok=True)
                        
                        if useImageLinks:
                                document.save_as_markdown(markdownPath, artifactDir, image_mode=ImageRefMode.REFERENCED, page_break_placeholder="----page-break-here----")
                                document.save_as_json(jsonPath, image_mode=ImageRefMode.PLACEHOLDER)

                        else:
                                document.save_as_markdown(markdownPath, artifactDir, image_mode=ImageRefMode.PLACEHOLDER, page_break_placeholder="----page-break-here----")
                                document.save_as_json(jsonPath, image_mode=ImageRefMode.PLACEHOLDER)

                        print(f"Generated markdown: {markdownPath} for {item['file']}")