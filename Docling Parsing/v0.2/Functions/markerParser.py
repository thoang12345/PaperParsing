from marker.converters.pdf import PdfConverter
from marker.renderers.markdown import MarkdownOutput
from marker.models import create_model_dict
from Functions import parsingProfiles
from Functions.utilities import logger, t
from pathlib import Path
import json
from typing import Any

class MarkerParser:
        def __init__(
                self,
                profile: parsingProfiles.markerPipelineOptions,
                ):
                self.profile = profile
                self.converter = self._buildPdfConverter(profile)

        @staticmethod
        def _buildPdfConverter(profile: parsingProfiles.markerPipelineOptions) -> PdfConverter:
                artifact_dict = create_model_dict()
                config = {
                        "force_ocr": profile.forceOCR,
                        "paginate_output": profile.paginateOutput,
                        "strip_existing_ocr": profile.stripExistingOCR,
                        "mode":  profile.mode,
                }

                if profile.pageRanges:
                        config["page_range"] = profile.pageRanges

                kwargs = {
                        "artifact_dict": artifact_dict,
                        "config": config,
                        }

                print(kwargs)

                if profile.useLLM:
                        config.update({
                                "use_llm": True,
                                "ollama_base_url": profile.ollamaBaseUrl,
                                "ollama_model": profile.ollamaModel,
                        })

                        kwargs["llm_service"] = profile.llmService

                return PdfConverter(**kwargs)


        def convert(self, pdf: Path) -> MarkdownOutput:
                return self.converter(str(pdf))

        def export(
                self,
                rendered: MarkdownOutput,
                outputFolder: Path,
                parserName: str,
                stem: str,
                ) -> dict[str, Any]:

                baseDir = outputFolder / "marker" / parserName
                outputDir = baseDir / stem

                outputDir.mkdir(parents=True, exist_ok=True)

                # Save markdown
                markdownPath = outputDir / f"{stem}.md"
                markdownPath.write_text(
                        rendered.markdown,
                        encoding="utf-8",
                )
                logger.info(f"Wrote {markdownPath}")

                # Save metadata
                jsonPath = outputDir / f"{stem}.json"
                with open(jsonPath, "w", encoding="utf-8") as f:
                        json.dump(rendered.metadata, f, indent=2)

                logger.info(f"Wrote {jsonPath}")

                # Save extracted images beside the markdown
                for imageName, image in rendered.images.items():
                        image.save(outputDir / imageName)

                logger.info(f"Wrote {len(rendered.images)} images")

                return {
                        "file": stem,
                        "parser": parserName,
                        "pages": self.converter.page_count,
                        "markdown": markdownPath,
                        "json": jsonPath,
                        "images": outputDir,
                }

def convertDocumentsMarker(
    parserPlans: list[dict[str, Any]],
    inputFolder: Path,
    outputFolder: Path,
) -> list[dict[str, Any]]:
    markerPlans = [
        plan
        for plan in parserPlans
        if plan["parser_plan"].startswith("marker")
    ]

    parsers: dict[str, MarkerParser] = {}
    results: list[dict[str, Any]] = []

    for plan in markerPlans:
        parserName = plan["parser_plan"]

        if parserName not in parsers:
            profile = parsingProfiles.getMarkerProfile(parserName)
            parsers[parserName] = MarkerParser(profile)

        parser = parsers[parserName]
        pdf = inputFolder / plan["file"]

        try:
            logger.info(f"Converting {pdf.name} with {parserName}")

            t.tic()
            rendered = parser.convert(pdf)
            logger.info(
                f"{pdf.name}: {parser.converter.page_count} pages"
            )
            t.toc(f"Converted {pdf.name} in")

            summary = parser.export(
                rendered,
                outputFolder,
                parserName,
                pdf.stem,
            )

            results.append(summary)

        except Exception:
            logger.exception(f"{parserName} failed on {pdf.name}")

    return results

