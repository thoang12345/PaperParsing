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

                basePath = outputFolder / "docling" / parserName 

                basePath.mkdir(parents=True, exist_ok=True)

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

                        markdownPath = basePath / stem / f"{stem}.md"
                        jsonPath = basePath / stem / f"{stem}.json"

                        (basePath / stem).mkdir(parents=True, exist_ok=True)

                        if useImageLinks:
                                document.save_as_markdown(
                                markdownPath,
                                artifacts_dir=basePath / stem,
                                image_mode=ImageRefMode.REFERENCED,
                                page_break_placeholder="----page-break-here----"
                                )
                        else:
                                document.save_as_markdown(
                                markdownPath,
                                artifacts_dir=basePath / stem,
                                image_mode=ImageRefMode.PLACEHOLDER,
                                page_break_placeholder="----page-break-here----"
                                )

                        document.save_as_json(
                                jsonPath,
                                image_mode=ImageRefMode.PLACEHOLDER
                        )

                        logger.info(f"Generated markdown: {markdownPath} for {item['file']}")