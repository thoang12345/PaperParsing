import os
from pathlib import Path
import torch
import time
import tiktoken
from transformers import pipeline

# Importing the DocumentConverter class from the docling library
from docling.document_converter import DocumentConverter
from docling_core.types.doc import ImageRefMode, PictureItem, TableItem, DocItemLabel, DoclingDocument, NodeItem, TextItem
from docling.datamodel.base_models import InputFormat, ItemAndImageEnrichmentElement
from docling.models.base_model import BaseItemAndImageEnrichmentModel
from docling.datamodel.accelerator_options import AcceleratorOptions, AcceleratorDevice
from docling.datamodel.pipeline_options import LayoutOptions, RapidOcrOptions, TableStructureOptions, EasyOcrOptions, TesseractOcrOptions, ThreadedPdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.layout_model_specs import DOCLING_LAYOUT_EGRET_LARGE
from docling_core.transforms.chunker.tokenizer.openai import OpenAITokenizer    
from docling.chunking import HybridChunker
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

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
    pipelineOptions.ocr_options = EasyOcrOptions(force_full_page_ocr=True) #Better Test
    pipelineOptions.layout_options = LayoutOptions(model_spec=DOCLING_LAYOUT_EGRET_LARGE, batch_size=configPiplineConfig.layoutBatchSize)

    return pipelineOptions

def initializeStuff(config):
    clear_terminal()
    pipelineOptions = buildPipelineOptions(config)
    tokenizer = OpenAITokenizer(tokenizer=tiktoken.encoding_for_model("gpt-4o"), max_tokens=128)
    print("Initialized tokenizer.")
    generator = pipeline("text-generation", model="Qwen/Qwen2.5-3B-Instruct", device=0 if torch.cuda.is_available() else -1)
    
    if checkAccelerator() == True:
        print("CUDA is available. Using GPU acceleration for conversion.")
        print(f"GPU: {torch.cuda.get_device_name(0)}")
    else:
        print("CUDA is not available. Using CPU for conversion, which may be slower.")
        
    converter = DocumentConverter(format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipelineOptions)})
    
    return converter, generator, tokenizer

def checkAccelerator():
    accelerator = False
    if torch.cuda.is_available():
        accelerator = True
    
    return accelerator

def convertFile(source, names, converter):
    start = time.time()
    
    print(f"\nStarting conversion of {len(source)} files...")
    print(f"Files being converted: {', '.join(Path(name).stem for name in names)}")
    results = list(converter.convert_all(source))

    end = time.time()
    elapsed = end - start
    hours = int(elapsed // 3600)
    mins = int((elapsed % 3600) // 60)
    secs = elapsed % 60
    
    print(f"Time taken to convert {len(source)} files: {hours:2.0f} h : {mins:2.0f} m : {secs:2.2f} s")
                
    return results

def writeItDown(result, outputPath, Name, addElements):
    folder = Path(outputPath) / Path(str(Name)).stem
    folder.mkdir(parents=True, exist_ok=True)
    
    mdPath = folder / f"{Path(Name).stem}_output.md"
    
    if addElements:
        print(f"Saving {Name} with elements as markdown...")
        try:
            result.document.save_as_markdown(mdPath, image_mode=ImageRefMode.REFERENCED)
        except OSError as e:
            print(f"Warning: Could not save images for {Name} ({e}), saving without image references...")
            result.document.save_as_markdown(mdPath)
    else:
        print(f"Saving {Name} as markdown...")
        result.document.save_as_markdown(mdPath)
    
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
    print(f"""Successful Conversions: {successOutOfTotal}
    Time taken to convert files: {hours:2.0f} h : {mins:2.0f} m : {secs:2.2f} s
    CUDA Used? {torch.cuda.is_available()}
    GPU: {torch.cuda.get_device_name(0)}
    {"=" * 100}
    Pipeline Options:
    {"=" * 100}
    Images Scale: {config.ImageScale}
    Generate Picture Images: {config.addElements}
    Do Formula Enrichment: {config.addElements}          
    Do Table Structure: {config.tableStructure}
    Do OCR: {config.doOcr}
    OCR Batch Size: {config.ocrBatchSize}
    Layout Batch Size: {config.layoutBatchSize}
    Table Batch Size: {config.tableBatchSize}
    {"=" * 100}""")
    
def folderFind(path, Name):
    folder = Path(path) / Name
    folder.mkdir(parents=True, exist_ok=True)
    
    return folder 

def filterParsed(file_paths, names, outputPath):
    filtered_paths = []
    filtered_names = []
    for i, name in enumerate(names):
        expected = Path(outputPath) / Path(name).stem / f"{Path(name).stem}_output.md"
        if expected.exists():
            print(f"Skipping {Path(name).stem} — already parsed.")
        else:
            filtered_paths.append(file_paths[i])
            filtered_names.append(name)
    print(f"{len(filtered_names)} files to convert, {len(names) - len(filtered_names)} skipped.\n")
    return filtered_paths, filtered_names

def chunkDocument(inputPath, generator, Name):
    folder = Path(inputPath) / Path(str(Name)).stem
    text = Path(folder / f"{Path(Name).stem}_output.md").read_text(encoding="utf-8")

    splitText = [('#', "H1"), ('##', "H2"), ('###', "H3"), ('####', "H4"), ('#####', "H5"), ('######', "H6")]
    mdSplitter = MarkdownHeaderTextSplitter(headers_to_split_on=splitText, strip_headers=False)
    headerChunks = mdSplitter.split_text(text)

    enc = tiktoken.encoding_for_model("gpt-4o")
    recursiveSplitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=128,
        length_function=lambda t: len(enc.encode(t)),
        separators=["\n\n", "\n", " ", ""]
    )
    finalChunks = recursiveSplitter.split_documents(headerChunks)

    for i, chunk in enumerate(finalChunks):
        headers = " > ".join(v for v in chunk.metadata.values() if v)
        
        prevSection = finalChunks[i - 1].page_content[-300:] if i > 0 else ""
        nextSection = finalChunks[i + 1].page_content[:300] if i < len(finalChunks) - 1 else ""
        prompt = (f"Previous Context: \n {prevSection}\n\n Current Context: \n {chunk.page_content}\n\n Next Context: \n {nextSection}\n\n"
                    f"In 2 sentences, write a summary of the current section informed by both the previous and next chunk."
                    if prevSection or nextSection else
                    f"Current Context: \n {chunk.page_content}\n\n In 2 sentences, write a summary of the current section."
                    )

        contextSummary = generator(prompt, max_new_tokens = 128, truncation=True)[0]['generated_text'].strip()
        
        if headers:
            chunk.page_content = f"[{headers}]\nContext: {contextSummary} \n\n{chunk.page_content}"
        else:
            chunk.page_content = f"Context: {contextSummary} \n\n{chunk.page_content}"
            
    return finalChunks

def writeChunksDown(input, outputPath, Name, generator):
        chunks = chunkDocument(input, generator, Name)
        folder = Path(outputPath) / Path(str(Name)).stem
        folder.mkdir(parents=True, exist_ok=True)

        with open(folder / f"{Path(Name).stem}_chunks.md", "w", encoding="utf-8") as f:
            for i, chunk in enumerate(chunks):
                f.write(f"=== Chunk {i} ===\n\n")
                f.write(chunk.page_content)
                f.write("\n\n")
    
        print(f"Wrote {len(chunks)} chunks to {outputPath}")


