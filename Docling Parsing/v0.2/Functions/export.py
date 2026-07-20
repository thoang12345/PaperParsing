from Functions.utilities import logger, t
from Functions import doclingParser

from pathlib import Path
from typing import Any
from docling_core.types.doc import ImageRefMode

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

                useImageLinks = doclingParser.doclingMarkdownUsesImages(profile)
        
                logger.info(f"\nResults from {parserName}")
                logger.info(f"Profile: {profile.name}")
                logger.info(f"Image links enabled: {useImageLinks}\n")

                for item, conversionResult in zip(batch, conversionGenerator):
                        document = conversionResult.document

                        if document is None:
                                logger.info(f"Skipping failed conversion: {item['file']}")
                                continue

                        sourceName = item["file"]
                        stem = Path(sourceName).stem

                        markdownDir = markdownOutput / stem
                        jsonDir = jsonOutput / stem
                        artifactDir = assetOutput / stem

                        markdownDir.mkdir(parents=True, exist_ok=True)
                        jsonDir.mkdir(parents=True, exist_ok=True)
                        artifactDir.mkdir(parents=True, exist_ok=True)

                        markdownPath = markdownDir / f"{stem}.md"
                        jsonPath = jsonDir / f"{stem}.json"

                        if useImageLinks:
                                document.save_as_markdown(
                                markdownPath,
                                artifacts_dir=artifactDir,
                                image_mode=ImageRefMode.REFERENCED,
                                page_break_placeholder="----page-break-here----"
                                )
                        else:
                                document.save_as_markdown(
                                markdownPath,
                                artifacts_dir=artifactDir,
                                image_mode=ImageRefMode.PLACEHOLDER,
                                page_break_placeholder="----page-break-here----"
                                )

                        document.save_as_json(
                                jsonPath,
                                image_mode=ImageRefMode.PLACEHOLDER
                        )

                        logger.info(f"Generated markdown: {markdownPath} for {item['file']}")