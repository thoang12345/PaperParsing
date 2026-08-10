from dataclasses import dataclass, field
from typing import Any
from enum import Enum

from docling.datamodel.pipeline_options import (
    EasyOcrOptions,
    RapidOcrOptions,
    LayoutOptions,
    TableFormerMode,
    TableStructureOptions,
    ThreadedPdfPipelineOptions,
    granite_picture_description,
)
from docling.datamodel.accelerator_options import (
    AcceleratorDevice,
    AcceleratorOptions,
)

from docling.datamodel.layout_model_specs import DOCLING_LAYOUT_EGRET_LARGE
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter, PdfFormatOption

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
        acceleratorDevice : str = "cuda"
        numberOfThreads : int = 4

        #safety/plugins
        allowExternalPlugins : bool = True

@dataclass(frozen=True)
class markerPipelineOptions:
    name: profileNames

    pageRanges: str | None = None

    forceOCR: bool = False
    paginateOutput: bool = True
    stripExistingOCR: bool = False

    useLLM: bool = False
    redoInlineMath: bool = False

    mode: str = "balanced"

    llmService: str | None = None

    ollamaBaseUrl: str = "http://localhost:11434"
    ollamaModel: str = "gemma4:e4b"

doclingProfiles: dict[profileNames, doclingPipelineOptions] = {
        profileNames.doclingNative: doclingPipelineOptions(
                name = profileNames.doclingNative,
                doOCR = True,
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
                numberOfThreads=2,
                doPictureDescriptions=True,
                pictureDescriptionPrompt=(
                "Always begin with 'Picture description:'. "
                "In 2–3 sentences, describe the figure type, its main content, and any important labels, values, or relationships. "
                "Be concise and factual."
                ),
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
                imageScale=1.25,
                doPictureDescriptions=True,
                pictureDescriptionPrompt=(
                "Always begin with 'Picture description:'. "
                "In 2–3 sentences, describe the figure type, its main content, and any important labels, values, or relationships. "
                "Be concise and factual."
                ),
        )
}

markerProfiles: dict[profileNames, markerPipelineOptions] = {
        profileNames.markerOCR: markerPipelineOptions(
                name=profileNames.markerOCR,
                forceOCR=False,
                paginateOutput=True,
                stripExistingOCR=False,
                useLLM=False,
        ),

        profileNames.markerOCRPlusLLM: markerPipelineOptions(
                name=profileNames.markerOCRPlusLLM,
                forceOCR=False,
                paginateOutput=True,
                stripExistingOCR=False,
                useLLM=True,
                redoInlineMath=True,
                llmService="marker.services.ollama.OllamaService",
                ollamaModel="gemma4:e4b",
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
                options.picture_description_options = granite_picture_description
                options.picture_description_options.prompt = profile.pictureDescriptionPrompt
                options.picture_description_options.generation_config = {
                        "max_new_tokens": 200,
                        "do_sample": False
                }      

        # Hardware
        options.accelerator_options = AcceleratorOptions(
                num_threads=profile.numberOfThreads,
                device=AcceleratorDevice(profile.acceleratorDevice),
        )

        # Plugins
        options.allow_external_plugins = profile.allowExternalPlugins

        return options

def buildDoclingConverterSettings(profile : doclingPipelineOptions) -> DocumentConverter:
        return DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(
                    pipeline_options=doclingSettings(profile)
                )
            }
        )

def addDoclingParserSettings(batchParserPlans : dict[str, list[list[dict[str, Any]]]]) -> dict[str, dict[str, Any]]:
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

        else:
            continue

        parserPlansWithSettings[parserName] = {
            "settings": settings,
            "profile": profile,
            "batches": parserBatches
        }

    return parserPlansWithSettings

def getMarkerProfile(parserName: str) -> markerPipelineOptions:
    profileMap = {
        "markerOCR": profileNames.markerOCR,
        "markerOCRPlusLLM": profileNames.markerOCRPlusLLM,
    }

    return markerProfiles[profileMap[parserName]]