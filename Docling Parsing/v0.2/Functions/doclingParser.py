from Functions import classify
from Functions.utilities import logger
from Functions import parsingProfiles
from Functions import export

from pathlib import Path
from typing import Any


def doclingMarkdownUsesImages(
    profile: parsingProfiles.doclingPipelineOptions,
) -> bool:
    return bool(
        profile.generatePictureImages
        or profile.generatePageImage
    )


def convertDocumentsDocling(
    parserPlans: list[dict[str, Any]],
    inputFolder: Path,
    outputFolder: Path,
) -> list[dict[str, Any]]:

    batches = classify.batchParserPlans(parserPlans)

    # Remove Marker plans
    batches.pop("markerOCR", None)
    batches.pop("markerOCRPlusLLM", None)

    batchPlans = parsingProfiles.addDoclingParserSettings(batches)

    results: list[dict[str, Any]] = []

    for parserName, plan in batchPlans.items():
        logger.info(f"Converting {parserName} plans")

        profile = plan["profile"]
        converter = plan["settings"]

        for batch in plan["batches"]:
            files = [
                inputFolder / item["file"]
                for item in batch
            ]

            logger.info(
                f"{parserName}: {[file.name for file in files]}"
            )

            convertedFiles = []

            for file in files:
                logger.info(f"Converting {file.name}")
                convertedFiles.append(converter.convert(file))

            batchResult = {
                "name": parserName,
                "profile": profile,
                "settings": converter,
                "result": convertedFiles,
                "batch": batch,
            }

            # Save immediately after each batch
            export.exportResults([batchResult], outputFolder)

            results.append(batchResult)

    return results