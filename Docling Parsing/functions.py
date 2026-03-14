import os
from pathlib import Path
import torch
import time
import fitz
from PIL import Image

# Importing the DocumentConverter class from the docling library
from docling.document_converter import DocumentConverter
from docling_core.types.doc import ImageRefMode, PictureItem, TableItem, DocItemLabel, DoclingDocument, NodeItem, TextItem
from docling.datamodel.base_models import InputFormat, ItemAndImageEnrichmentElement
from docling.models.base_model import BaseItemAndImageEnrichmentModel
from docling.datamodel.accelerator_options import AcceleratorOptions, AcceleratorDevice
from docling.datamodel.pipeline_options import LayoutOptions, RapidOcrOptions, TableStructureOptions, EasyOcrOptions, TesseractOcrOptions, ThreadedPdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.layout_model_specs import DOCLING_LAYOUT_EGRET_LARGE

pix2texModel = None

def clear_terminal():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')
        
def gimmeFileNames(path, includeFolders=False):
    folder = Path(path)
    if includeFolders:
        names = [item.name for item in folder.iterdir()]
    else:
        names = [file.name for file in folder.iterdir() if file.is_file()]
    return names

def buildFilePaths(path):
    fileNames = gimmeFileNames(path)
    filePath = []
    
    for files in fileNames:
        filePath.append(os.path.join(path, files))
        
    return filePath

def buildPipelineOptions(configPiplineConfig):
    pipelineOptions = ThreadedPdfPipelineOptions()
    pipelineOptions.images_scale = configPiplineConfig.ImageScale
    pipelineOptions.generate_picture_images = configPiplineConfig.addElements
    pipelineOptions.do_formula_enrichment = configPiplineConfig.addElements
    pipelineOptions.generate_page_images = configPiplineConfig.addElements
    pipelineOptions.do_table_structure = True
    pipelineOptions.table_structure_options = TableStructureOptions(do_cell_matching=configPiplineConfig.tableStructure)
    pipelineOptions.do_ocr = configPiplineConfig.doOcr 
    pipelineOptions.accelerator_options = AcceleratorOptions(AcceleratorDevice.AUTO, num_threads=4)
    pipelineOptions.ocr_batch_size = configPiplineConfig.ocrBatchSize       
    pipelineOptions.layout_batch_size = configPiplineConfig.layoutBatchSize    
    pipelineOptions.table_batch_size = configPiplineConfig.tableBatchSize
    #pipelineOptions.ocr_options = TesseractOcrOptions(force_full_page_ocr=True) #Buns
    #pipelineOptions.ocr_options = RapidOcrOptions(force_full_page_ocr=True) #Better Equations
    pipelineOptions.ocr_options = EasyOcrOptions(force_full_page_ocr=True) #Better Test
    pipelineOptions.layout_options = LayoutOptions(model_spec=DOCLING_LAYOUT_EGRET_LARGE, batch_size=configPiplineConfig.layoutBatchSize)

    return pipelineOptions

def initializeStuff(config):
    clear_terminal()
    pipelineOptions = buildPipelineOptions(config)
    checkAccelerator()
    
    return pipelineOptions

def checkAccelerator():
    if torch.cuda.is_available():
        print(f"CUDA is available.\nUsing GPU: {torch.cuda.get_device_name(0)}\n")
    else:
        print("CUDA is not available. Using CPU.")

def convertFile(source, Name, pipelineOptions):
    start = time.time()
    
    print(f"\nStarting conversion of {Path(str(Name)).stem}...")
    
    converter = DocumentConverter(format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipelineOptions)})
    result = converter.convert(source) 
    
    end = time.time()
    elapsed = end - start
    hours = int(elapsed // 3600)
    mins = int((elapsed % 3600) // 60)
    secs = elapsed % 60
    
    print(f"Time taken to convert {Path(str(Name)).stem}: {hours:2.0f} h : {mins:2.0f} m : {secs:2.2f} s")
                
    return result

def writeItDown(result, outputPath, Name, addElements):
    folder = Path(outputPath) / Path(str(Name)).stem
    folder.mkdir(parents=True, exist_ok=True)
    
    if addElements:
        result.document.save_as_markdown(folder / f"{Path(Name).stem}_output.md", image_mode=ImageRefMode.REFERENCED)
    else:    
        result.document.save_as_markdown(folder / f"{Path(Name).stem}_output.md")
    
def successfulConversions(inputPath, outputPath):
    totalFiles = len(gimmeFileNames(inputPath))
    successfulFiles = len(gimmeFileNames(outputPath, includeFolders=True))

    successOutofTotal = f"{successfulFiles}/{totalFiles}"
        
    return successOutofTotal

def printRunStats(inputPath, outputPath, startTime, endTime, config):    
    elapsed = endTime - startTime
    hours = int(elapsed // 3600)
    mins = int((elapsed % 3600) // 60)
    secs = elapsed % 60
    successOutOfTotal = successfulConversions(inputPath, outputPath)
    
    print("=" * 100)
    print(f"Successful Conversions: {successOutOfTotal}")
    print(f"Time taken to convert files: {hours:2.0f} h : {mins:2.0f} m : {secs:2.2f} s")
    print(f"CUDA Used? {torch.cuda.is_available()}")
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print("=" * 100)
    print("Pipeline Options:")
    print("=" * 100)
    print(f"Images Scale: {config.ImageScale}")
    print(f"Generate Picture Images: {config.addElements}")
    print(f"Do Formula Enrichment: {config.addElements}")
    print(f"Do Table Structure: {config.tableStructure}")
    print(f"Do OCR: {config.doOcr}")
    print(f"OCR Batch Size: {config.ocrBatchSize}")
    print(f"Layout Batch Size: {config.layoutBatchSize}")
    print(f"Table Batch Size: {config.tableBatchSize}")
    print("=" * 100)
    

def returnFormulas(path, Name, file, convertedFile):
    padding = 10
    filePath = folderFind(path, Path(str(Name)).stem)
    formulaImages = folderFind(path, Path(str(Name)).stem) / "Formulas"
    formulaImages.mkdir(exist_ok=True)
    pdf = fitz.open(file)
    formulaCount = 1
    
    for item, _ in convertedFile.document.iterate_items():
        if isinstance(item, TextItem) and item.label == DocItemLabel.FORMULA:
            pageNum = item.prov[0].page_no
            pageImage = convertedFile.document.pages[pageNum].image.pil_image
            
            bbox = item.prov[0].bbox
            print(f"Found formula at: Top={bbox.t}, Left={bbox.l}")
            print(f"Content: {item.text}")

            croppedImage = pageImage.crop((bbox.l, bbox.b, bbox.r, bbox.t))
            
            croppedImage.save(formulaImages / f"{Path(str(Name)).stem}_formula_{formulaCount}.png")
            formulaCount += 1
    
def folderFind(path, Name):
    folder = Path(path) / Name
    folder.mkdir(parents=True, exist_ok=True)
    
    return folder 