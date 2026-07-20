from Functions import classify
from Functions.utilities import logger, t
from Functions import parsingProfiles
from Functions import export

from pathlib import Path
from typing import Any
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer
from docling.chunking import HybridChunker

def convertDocumentsDocling(pdfClassification : list[dict[str : str, str : str, str : str]], not_pdfs : list[dict[str : str, str : str, str : str]], inputFolder : Path, outputFolder : Path, chunkingTools : list[HybridChunker, HuggingFaceTokenizer]) -> list[dict[str, Any]]:
        parserPlans = classify.chooseParserPlan(pdfClassification, not_pdfs)
        sortedParserPlans = sorted(parserPlans, key=lambda x: x["parser_plan"])
        batches = classify.batchParserPlans(sortedParserPlans)
        batches.pop("markerOCR", None)
        batches.pop("markerOCRPlusLLM", None)
        batchPlans = parsingProfiles.addParserPlansSettings(batches)
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

        export.exportResults(results, outputFolder)

        return results

def doclingMarkdownUsesImages(profile: parsingProfiles.doclingPipelineOptions) -> bool:
        return bool(profile.generatePictureImages or profile.generatePageImage)