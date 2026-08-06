from Functions.utilities import logger, t
from Functions.parsingProfiles import profileNames
from Functions import paths
from pathlib import Path
import json

from docling.chunking import HybridChunker
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer
from docling_core.types.doc.document import DoclingDocument
from docling_core.transforms.chunker import DocChunk
from docling_core.types.doc.document import TableItem, PictureItem

def chunkDocuments(outputFolder: Path, pdfClassification : list[dict[str : str, str : str, str : str]], 
                   not_pdfs : list[dict[str : str, str : str, str : str]],
                   doclingChunkingTools : tuple[HybridChunker, HuggingFaceTokenizer]
                   ) -> dict[str, list]:
        parserOutput = paths.findOutputFiles(outputFolder, pdfClassification, not_pdfs)

        chunkOutput = {item.value: [] for item in profileNames}

        for output in parserOutput:
                file = output["file"]
                name = Path(file).stem
                parserPlan = output["parser_plan"]
                JSON = (output["output"])["JSON"]
                markdown = (output["output"])["markdown"]

                if JSON is None:
                        logger.warning(f"Missing JSON for {name}, skipping")
                        continue

                if parserPlan == "doclingNative":
                        chunks = nativeHybridChunker(name, parserPlan, JSON, doclingChunkingTools)
                        chunkOutput["doclingNative"].append(chunks)

                        logger.info(f"Sucessfully chunked {len(chunkOutput["doclingNative"])} {parserPlan} documents")
                elif parserPlan == "doclingOCR":
                        chunks = OCRHybridChunker(name, parserPlan, JSON, doclingChunkingTools)
                        chunkOutput["doclingOCR"].append(chunks)

                        logger.info(f"Sucessfully chunked {len(chunkOutput["doclingOCR"])} {parserPlan} documents")
                elif parserPlan == "doclingScannedOCR":
                        chunks = OCRHybridChunker(name, parserPlan, JSON, doclingChunkingTools)
                        chunkOutput["doclingScannedOCR"].append(chunks)

                        logger.info(f"Sucessfully chunked {len(chunkOutput["doclingScannedOCR"])} {parserPlan} documents")

                else:
                        logger.info(f"No chunking plan for {name} with {parserPlan} profile.")

        return chunkOutput

def buildAllChunks(document : DoclingDocument, name : str, plan : str, doclingTools : tuple[HybridChunker, HuggingFaceTokenizer]) -> dict:
        chunker = doclingTools[0]
        tokenizer = doclingTools[1]

        t.tic()

        chunks = list(chunker.chunk(dl_doc=document))

        fileOutput = []
        chunksOutput = []

        for chunkNumber, chunk in enumerate(chunks):
                chunkMetadata = buildChunkMetadata(chunk, chunkNumber, name, plan, tokenizer, chunker)
                chunkText = chunk.text

                isTable = any(isinstance(item, TableItem) for item in chunk.meta.doc_items)
                isPicture = any(isinstance(item, PictureItem) for item in chunk.meta.doc_items)

                if isTable:
                        chunkMetadata["chunkType"] = "table"
                elif isPicture:
                        chunkMetadata["chunkType"] = "picture"
                else:
                        chunkMetadata["chunkType"] = "text"        

                chunksOutput.append({
                        "text":chunkText,
                        "metadata":chunkMetadata                
                        }
                )

        fileOutput = {
                "name" : name,
                "chunks" : chunksOutput
                }
                
        t.toc(f"Chunked {name} with {plan} producing {len(chunks)} chunks in")

        return fileOutput

def buildChunkMetadata(chunk : DocChunk, chunkNumber : int, name : str, plan : str, tokenizer : HuggingFaceTokenizer, chunker: HybridChunker):
        pageNumbers = set()
        classifications = set()
        pictureDescription = None

        headings = chunk.meta.headings if chunk.meta.headings else []

        for item in chunk.meta.doc_items:
                if hasattr(item, "label") and item.label:
                        classifications.add(str(item.label))

                for provenance in getattr(item, "prov", []):
                        if hasattr(provenance, "page_no"):
                                pageNumbers.add(provenance.page_no)

                if isinstance(item, PictureItem):
                        if item.meta is not None and item.meta.description is not None:
                                pictureDescription = item.meta.description.text

        tokenCount = tokenizer.count_tokens(chunk.text)

        try:
                contextualizeChunk = chunker.contextualize(chunk=chunk)
        except Exception:
                contextualizeChunk = chunk.text

        return {
                "paperName":name,
                "parserPlan":plan,
                "headings":headings,
                "pageNumbers":sorted(list(pageNumbers)),
                "classifications":list(classifications),
                "tokenCount":tokenCount,
                "contextualize":contextualizeChunk,
                "chunkNumber":chunkNumber,
                "pictureDescription": pictureDescription
        }

def nativeHybridChunker(name : str, plan : str, JSON : Path, doclingTools : tuple[HybridChunker, HuggingFaceTokenizer]) -> dict:
        document = DoclingDocument.model_validate(json.loads(JSON.read_text(encoding="utf-8")))
        fileOutput = buildAllChunks(document, name, plan, doclingTools)
        
        return fileOutput               

def OCRHybridChunker(name: str, plan: str, JSON: Path, doclingTools: tuple) -> dict:
        document = DoclingDocument.model_validate(json.loads(JSON.read_text(encoding="utf-8")))
        fileOutput = buildAllChunks(document, name, plan, doclingTools)
               
        return fileOutput   
