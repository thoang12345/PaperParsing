from Functions.utilities import logger, t
from Functions.parsingProfiles import profileNames
from Functions import paths
from pathlib import Path
import json
from transformers import pipeline

from docling.chunking import HybridChunker
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer
from docling_core.types.doc.document import DoclingDocument


def chunkDocuments(outputFolder: Path, pdfClassification : list[dict[str : str, str : str, str : str]], 
                   not_pdfs : list[dict[str : str, str : str, str : str]],
                   doclingChunkingTools : tuple[HybridChunker, HuggingFaceTokenizer],
                   generator : pipeline
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
                        chunks = OCRHybridChunker(name, parserPlan, JSON, doclingChunkingTools, generator)
                        chunkOutput["doclingOCR"].append(chunks)

                        logger.info(f"Sucessfully chunked {len(chunkOutput["doclingOCR"])} {parserPlan} documents")
                elif parserPlan == "doclingScannedOCR":
                        chunks = OCRHybridChunker(name, parserPlan, JSON, doclingChunkingTools, generator)
                        chunkOutput["doclingScannedOCR"].append(chunks)

                        logger.info(f"Sucessfully chunked {len(chunkOutput["doclingScannedOCR"])} {parserPlan} documents")

                else:
                        logger.info(f"No chunking plan for {name} with {parserPlan} profile.")

        return chunkOutput

def nativeHybridChunker(name : str, plan : str, JSON : Path, doclingTools : tuple[HybridChunker, HuggingFaceTokenizer]) -> dict:
        chunker = doclingTools[0]
        tokenizer = doclingTools[1]

        t.tic()
        with open(JSON, "r", encoding="utf-8") as f:
                data = json.load(f)

        document = DoclingDocument.model_validate(data)
        chunks = list(chunker.chunk(dl_doc=document))

        fileOutput = []
        chunksOutput = []
        

        for chunkNumber, chunk in enumerate(chunks):
                pageNumbers = set()
                classifications = set()
                for item in chunk.meta.doc_items:
                        if hasattr(item, "label") and item.label:
                                classifications.add(str(item.label))
                        for provenance in getattr(item, "prov", []):
                                if hasattr(provenance, "page_no"):
                                        pageNumbers.add(provenance.page_no)

                sortedPages = sorted(list(pageNumbers))
                tokenCount = tokenizer.count_tokens(chunk.text)
                headings = chunk.meta.headings if chunk.meta.headings else []

                try:
                        contextualizeChunk = chunker.contextualize(chunk=chunk)
                except Exception:
                        contextualizeChunk = chunk.text

                chunksOutput.append({
                        "text" : chunk.text,
                        "metadata" : {
                                "paperName" : name,
                                "parsingPlan": plan,
                                "headings" : headings,
                                "pageNumbers" : sortedPages,
                                "classifications" : list(classifications),
                                "tokenCount" : tokenCount,
                                "contextualize" : contextualizeChunk,
                                "chunkNumber" : chunkNumber,
                        }
                })

        fileOutput = {
                "name" : name,
                "chunks" : chunksOutput
                }
                
        t.toc(f"Chunked {name} with {plan} producing {len(chunks)} chunks in")
        return fileOutput                        

def OCRHybridChunker(name: str, plan: str, JSON: Path, doclingTools: tuple, generator : pipeline) -> dict:
        chunker = doclingTools[0]
        tokenizer = doclingTools[1]

        t.tic()
        with open(JSON, "r", encoding="utf-8") as f:
                data = json.load(f)

        document = DoclingDocument.model_validate(data)
        chunks = list(chunker.chunk(dl_doc=document))

        fileOutput = []
        chunksOutput = []
        

        for chunkNumber, chunk in enumerate(chunks):
                pageNumbers = set()
                classifications = set()
                for item in chunk.meta.doc_items:
                        if hasattr(item, "label") and item.label:
                                classifications.add(str(item.label))
                        for provenance in getattr(item, "prov", []):
                                if hasattr(provenance, "page_no"):
                                        pageNumbers.add(provenance.page_no)

                sortedPages = sorted(list(pageNumbers))
                tokenCount = tokenizer.count_tokens(chunk.text)
                headings = chunk.meta.headings if chunk.meta.headings else []

                try:
                        contextualizeChunk = chunker.contextualize(chunk=chunk)
                except Exception:
                        contextualizeChunk = chunk.text

                chunksOutput.append({
                        "text" : chunk.text,
                        "metadata" : {
                                "paperName" : name,
                                "parsingPlan": plan,
                                "headings" : headings,
                                "pageNumbers" : sortedPages,
                                "classifications" : list(classifications),
                                "tokenCount" : tokenCount,
                                "contextualize" : contextualizeChunk,
                                "chunkNumber" : chunkNumber,
                        }
                })

        fileOutput = {
                "name" : name,
                "chunks" : chunksOutput
                }
                
        t.toc(f"Chunked {name} with {plan} producing {len(chunks)} chunks in")
        return fileOutput

def generateArtifactContext(generator, prev_section: str, current_content: str, next_section: str) -> str:
        """
        Takes the surrounding text chunks and the current artifact,
        and uses the LLM to generate a clean 2-3 sentence summary.
        """
        prompt = (
                f"<|im_start|>system\n"
                f"You are a precise academic summarizer. Your only job is to write a single, clean 2-3 sentence summary of the current chunk. "
                f"Use the previous and next chunks only to inform your understanding — do not summarize them. "
                f"Rules: no markdown, no bullet points, no headers, no newlines, no internal thoughts, no meta-commentary, no repetition of these instructions. "
                f"Output only the summary paragraph and nothing else.<|im_end|>\n"
                f"<|im_start|>user\n"
                f"Previous chunk:\n{prev_section}\n\n"
                f"Current chunk:\n{current_content}\n\n"
                f"Next chunk:\n{next_section}\n"
                f"<|im_end|>\n"
                f"<|im_start|>assistant\n"
        )

        generation = generator(prompt, max_new_tokens=150, return_full_text=False)
        return generation[0]["generated_text"].strip()