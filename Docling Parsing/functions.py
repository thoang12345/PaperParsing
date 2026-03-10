import os
from pathlib import Path
import re
import pandas as pd

# Importing the DocumentConverter class from the docling library
from docling.document_converter import DocumentConverter
from docling_core.types.doc import ImageRefMode, PictureItem, TableItem, DocItemLabel
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, RapidOcrOptions, TableStructureOptions, EasyOcrOptions, TesseractOcrOptions
from docling.document_converter import DocumentConverter, PdfFormatOption


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

def pipelineOptions(ImageScale, generatePictureImages, doFormulas, doOcr):
    pipelineOptions = PdfPipelineOptions()
    pipelineOptions.images_scale = ImageScale
    pipelineOptions.generate_picture_images = generatePictureImages
    pipelineOptions.do_formula_enrichment = doFormulas
    pipelineOptions.do_table_structure = True
    pipelineOptions.table_structure_options = TableStructureOptions(do_cell_matching=True)
    pipelineOptions.do_ocr = doOcr
    #pipelineOptions.ocr_options = TesseractOcrOptions(force_full_page_ocr=True)
    #pipelineOptions.ocr_options = RapidOcrOptions(force_full_page_ocr=True)
    #pipelineOptions.ocr_options = EasyOcrOptions(force_full_page_ocr=True)

    return pipelineOptions

def convertFile(source, pipelineOptions):
    converter = DocumentConverter(format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipelineOptions)})
    result = converter.convert(source) 
                
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

def printRunStats(inputPath, outputPath, startTime, endTime):
    clear_terminal()
    
    elapsed = endTime - startTime
    mins = elapsed // 60
    secs = elapsed % 60
    successOutOfTotal = successfulConversions(inputPath, outputPath)
    
    print("=" * 100)
    print(f"Successful Conversions: {successOutOfTotal}")
    print(f"Time taken to convert files: {mins:2.0f} m and {secs:2.2f} s")
    print("=" * 100)
    
def returnFormulas(path, Name, convertedFile):
    formulas = []
    for element, _level in convertedFile.document.iterate_items():
        if element.label == DocItemLabel.FORMULA:
            formulas.append(element.text)
    
    folder = Path(path) / Path(str(Name)).stem
    folder.mkdir(parents=True, exist_ok=True)
    mdFilename = folder / f"{Path(Name).stem}_output.md"
    mdContent = mdFilename.read_text(encoding="utf-8")
    
    if not formulas:
        print(f"No formulas found for {Path(str(Name)).stem}")
    else:
        for formula in formulas:
            mdContent = mdContent.replace("<!-- formula-not-decoded -->", f"$${formula}$$", 1)
        print(f"{len(formulas)} formulas returned for {Path(str(Name)).stem}")    
    mdFilename.write_text(mdContent,encoding="utf-8")
    
    