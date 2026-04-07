import os
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"  # also block huggingface_hub specifically

from pathlib import Path
import torch
import time
import tiktoken
from transformers import pipeline
import warnings
from transformers import logging as hf_logging
import chromadb

hf_logging.set_verbosity_error()
warnings.filterwarnings("ignore", message=".*max_new_tokens.*max_length.*")

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
    pipelineOptions.allow_external_plugins = True

    return pipelineOptions

def initializeStuff(config):
    clear_terminal()
    pipelineOptions = buildPipelineOptions(config)
    tokenizer = OpenAITokenizer(tokenizer=tiktoken.encoding_for_model("gpt-4o"), max_tokens=128)
    print("Initialized tokenizer.")
    generator = pipeline("text-generation", model="Qwen/Qwen2.5-3B-Instruct", device=0 if torch.cuda.is_available() else -1)
    databaseClient = chromadb.PersistentClient(path="./chroma_db")
    print("Initialized generator and database client.")
    
    if checkAccelerator() == True:
        print("CUDA is available. Using GPU acceleration for conversion.")
        print(f"GPU: {torch.cuda.get_device_name(0)}\n")
    else:
        print("CUDA is not available. Using CPU for conversion, which may be slower.\n")
        
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
    timeTaken = convertTime(start, end)
    
    print(f"Time taken to convert {len(source)} files: {timeTaken}\n")
                
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
    
def successfulConversions(numResults, numParsed):
    successOutofTotal = f"{numResults}/{numParsed}"
        
    return successOutofTotal

def printRunStats(startTime, endTime, config, numParsed, numResults):    
    timeTaken = convertTime(startTime, endTime)
    successOutOfTotal = successfulConversions(numResults, numParsed)
    
    print("=" * 100)
    print(f"""Successful Conversions: {successOutOfTotal}
Time taken to convert files: {timeTaken}
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
    print(f"{len(filtered_names)} files to convert, {len(names) - len(filtered_names)} skipped.")
    return filtered_paths, filtered_names, len(filtered_names)

def chunkDocument(inputPath, Name):
    print(f"Chunking {Name}...")
    
    folder = Path(inputPath) / Path(str(Name)).stem
    text = Path(folder / f"{Path(Name).stem}_output.md").read_text(encoding="utf-8")
    startTime = time.time()
    splitText = [('#', "H1"), ('##', "H2"), ('###', "H3"), ('####', "H4"), ('#####', "H5"), ('######', "H6")]
    mdSplitter = MarkdownHeaderTextSplitter(headers_to_split_on=splitText, strip_headers=False)
    headerChunks = mdSplitter.split_text(text)

    enc = tiktoken.encoding_for_model("gpt-4o")
    recursiveSplitter = RecursiveCharacterTextSplitter(
        chunk_size=1024,
        chunk_overlap=256,
        length_function=lambda t: len(enc.encode(t)),
        separators=["\n\n", "\n", " ", ""]
    )
    finalChunks = recursiveSplitter.split_documents(headerChunks)
    promptBatch = batchPrompts(finalChunks)
            
    return finalChunks, startTime, promptBatch

def writeChunksDown(chunks, summaries, prompts, outputPath, Name, startTime):
        folder = Path(outputPath) / Path(str(Name)).stem
        folder.mkdir(parents=True, exist_ok=True)
        
        contextSummary = ""
        
        for i, chunk in enumerate(chunks):
                headers = " > ".join(v for v in chunk.metadata.values() if v)
                raw = summaries[i][0]['generated_text'].strip()
                if prompts[i] in raw:
                    contextSummary = raw[len(prompts[i]):].strip()
                if headers:
                    chunk.page_content = f"[{headers}][Paper Name: {Name}]\nContext:\n{contextSummary} \n\n{chunk.page_content}"
                else:
                    chunk.page_content = f"Context: {contextSummary} \n\n{chunk.page_content}"

        with open(folder / f"{Path(Name).stem}_chunks.md", "w", encoding="utf-8") as f:
            for i, chunk in enumerate(chunks):
                f.write("\n"+("=" * 100))
                f.write(f"\n=== Chunk {i}===\n\n")
                f.write(chunk.page_content)
                f.write("\n")

        endTime = time.time()
        timeTaken = convertTime(startTime, endTime)
        print(f"Wrote {len(chunks)} chunks to {outputPath}/{Name}!\n")
        print(f"Time taken to chunk and write {Name}: {timeTaken}")

def batchPrompts(chunks):
    promptBatch = []
    
    for i, chunk in enumerate(chunks):
        prevSection = chunks[i - 1].page_content[-300:] if i > 0 else ""
        nextSection = chunks[i + 1].page_content[:300] if i < len(chunks) - 1 else ""
        prompt = (f"Previous Context: \n {prevSection}\n\nCurrent Context: \n {chunk.page_content}\n\nNext Context: \n {nextSection}\n\n"
                    f"In 1 uninterrupted section consisting of 3 sentences, write a summary of the current section informed by both the previous and next chunk." 
                    f"Just add the summary, no other preamble, or repeated information. Make a clean paragraph with no newlines, no enters, or no nextlines. Next lines will be handled in post processing. If there is no previous or next section, just summarize the current section.`"
                    f"When writing something about headers, only use the header text itself, not the markdown syntax. For example, if the header is '## Introduction', just use 'Introduction' in your summary and do not include the '##' markdown syntax."
                    f"Do not mention your instructions or anything about the prompt in the summary. Just write a clean summary paragraph that could be easily read on its own without any context about the prompt or instructions."
                    f"Do not include your internal thoughts or reasoning steps in the summary. Just write the final summary paragraph that directly summarizes the content of the current chunk, informed by the previous and next chunks if they exist."
                    if prevSection or nextSection else
                    f"Current Context: \n {chunk.page_content}\n\n In 3 sentences, write a summary of the current section."
                    )
        promptBatch.append(prompt)

    return promptBatch

def convertTime(start, end):
    seconds = end - start
    hours = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hours:2.0f} h : {mins:2.0f} m : {secs:2.2f} s"




