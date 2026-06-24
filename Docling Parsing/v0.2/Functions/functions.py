from __future__ import annotations
from pathlib import Path
import profile
import zipfile
from bs4 import BeautifulSoup
from httpx import options
from Functions import functionsClassify as pdfFun
from dataclasses import dataclass
from enum import Enum
from typing import Any
import torch
import time

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
                if pdf["content_type"] == "scientific" and pdf["text_type"] == "mixedPDF":
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

def markerSettings(pdfClassifications : list[dict[str : str, str : str, str : str]], generalClassifications : list[dict[str : str, str : str, str : str]]):
        ...

def buildPDFConverterSettings(profile : doclingPipelineOptions) -> DocumentConverter:
        return DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(
                    pipeline_options=doclingSettings(profile)
                )
            }
        )

def convertPDFsDocling(pdfClassification : list[dict[str : str, str : str, str : str]], not_pdfs : list[dict[str : str, str : str, str : str]], inputFolder : Path) -> dict[str : str]:
        parserPlans = chooseParserPlan(pdfClassification, not_pdfs)
        sortedParserPlans = sorted(parserPlans, key=lambda x: x["parser_plan"])
        batches = batchParserPlans(sortedParserPlans)
        batches.pop("markerOCR", None)
        batchPlans = addParserPlansSettings(batches)
        results = []
        
        for parserName, plan in batchPlans.items():
                print(f"Converting {parserName} plans")
                converter = plan["settings"]

                for batch in plan["batches"]:
                        files = [inputFolder / item["file"]for item in batch]

                        print(f"{parserName}: {[item.name for item in files]}")
                        convertedFile = converter.convert_all(files)
                        results.append({
                                "name" : parserName,
                                "result" : convertedFile,
                                "batch" : batch
                        })

        return results

def addParserPlansSettings(batchParserPlans : dict[str, list[list[dict[str, Any]]]]) -> dict[str,dict[str,DocumentConverter | list[list[dict[str, str]]]]]:
    parserPlansWithSettings = {}

    for parserName, parserBatches in batchParserPlans.items():
        if parserName == "doclingOCR":
            settings = buildPDFConverterSettings(doclingProfiles[profileNames.doclingOCR])

        elif parserName == "doclingScannedOCR":
            settings = buildPDFConverterSettings(doclingProfiles[profileNames.doclingScannedOCR])

        elif parserName == "doclingNative":
            settings = buildPDFConverterSettings(doclingProfiles[profileNames.doclingNative])

        else:
            continue

        parserPlansWithSettings[parserName] = {
            "settings": settings,
            "batches": parserBatches
        }

    return parserPlansWithSettings

def batchParserPlans(parserPlans : list[dict[str, str]]) -> dict[str, list[list[dict[str, Any]]]]:
        batches = {}
        batchSizes = {
                "doclingScannedOCR": 1,
                "doclingOCR": 2,
                "doclingNative": 8,
                "markerOCR": 1,
        }
        
        for item in parserPlans:
                parser = item["parser_plan"]
                parserBatchSize = batchSizes.get(parser, 1)

                parser_batches = batches.setdefault(parser, [])

                if not parser_batches or len(parser_batches[-1]) >= parserBatchSize:
                        parser_batches.append([])

                parser_batches[-1].append(item)

        return batches





