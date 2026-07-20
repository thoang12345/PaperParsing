from Functions import parsingProfiles
from Functions import classify

import shutil
import subprocess
from pathlib import Path
from typing import Any

def runMarkerCLI(batch: list[dict[str, str]], inputFolder: Path, outputFolder: Path, profile : parsingProfiles.markerPipelineOptions, parserName: str, batchNumber : int, outputFormat: str) -> dict[str, Any]:
        stageDirectory = outputFolder / "_markerStage" / parserName / f"batch_{batchNumber:03d}"
        resultDirectory = outputFolder / "marker" / parserName / outputFormat
        
        if stageDirectory.exists():
                shutil.rmtree(stageDirectory)

        resultDirectory.mkdir(parents=True, exist_ok=True)
        stageDirectory.mkdir(parents=True, exist_ok=True)

        for file in batch:
               sourcePath = inputFolder / file["file"]
               destinationPath = stageDirectory / file["file"]
               shutil.copy2(sourcePath, destinationPath)

        command = [
                "marker", str(stageDirectory),
                "--output_dir", str(resultDirectory),
                "--output_format", outputFormat,
                "--workers", str(profile.workers)
                ]
        
        if profile.forceOCR:
               command.append("--force_ocr")
        if profile.paginateOutput:
               command.append("--paginate_output")
        if profile.useLLM:
                command.append("--use_llm")
                command.extend([
                        "--llm_service", profile.llmService,
                        "--ollama_base_url", profile.ollamaBaseURL,
                        "--ollama_model", profile.ollamaModel,
                ])
                if profile.redoInlineMath:
                        command.append("--redo_inline_math")
        if profile.pageRanges is not None:
               command.extend(["--page_ranges", profile.pageRanges])
        if profile.stripExistingOCR:
               command.append("--strip_existing_ocr")

        completed = subprocess.run(command, check=True)

        summary = {
               "parserName": parserName,
               "batchNumber": batchNumber,
               "outputFormat": outputFormat,
               "stageDirectory": stageDirectory,
               "outputDirectory": resultDirectory,
               "command": command,
               "returnCode": completed.returncode,
               "stdout": completed.stdout,
               "stderr": completed.stderr,
               "batch": batch
        }

        return summary

def convertPDFsMarker(pdfClassification : list[dict[str : str, str : str, str : str]], not_pdfs : list[dict[str : str, str : str, str : str]], inputFolder : Path, outputFolder : Path) -> list[dict[str, str]]:
        parserPlans = classify.chooseParserPlan(pdfClassification, not_pdfs)
        sortedParserPlans = sorted(parserPlans, key=lambda x: x["parser_plan"])
        markerPlans = [item for item in sortedParserPlans if item["parser_plan"].startswith("marker")]
        batches = classify.batchParserPlans(markerPlans)
        batchPlans = parsingProfiles.addParserPlansSettings(batches)
        results = []
        
        for parserName, plan in batchPlans.items():
                settings = plan["settings"]
                batches = plan["batches"]

                for batchNumber, batch in enumerate(batches, start=1):
                       for outputFormat in settings.outputFormat:
                                result = runMarkerCLI(
                                        batch=batch,
                                        inputFolder=inputFolder,
                                        outputFolder=outputFolder,
                                        profile=settings,
                                        parserName=parserName,
                                        batchNumber=batchNumber,
                                        outputFormat=outputFormat,
                                )

                                results.append(result)

                                if result["returnCode"] != 0:
                                        raise RuntimeError(
                                                f"Marker failed for {parserName} batch {batchNumber} "
                                                f"with output format {outputFormat}\n\n"
                                                f"{result['stderr']}"
                                        )
        return results