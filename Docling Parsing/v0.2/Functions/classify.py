from Functions import functionsClassify as pdfFun
from Functions import paths
from Functions.utilities import logger, t
import zipfile
from pathlib import Path
from bs4 import BeautifulSoup
from typing import Any

def separatePDFs(path : Path) -> tuple[list[Path], list[Path]]:
        files = paths.parseFiles(path)
        pdfs = paths.filterPDFs(path)
        not_pdfs = [pdf for pdf in files if not pdf.endswith((".pdf", ".doc", ".ppt", ".xls"))]
        
        return pdfs, not_pdfs

def classifyPDFs(path : Path) -> list[dict[str : str, str : str, str : str]]:
        pdfs, not_pdfs = separatePDFs(path)
        pageData = pdfFun.extractPageData(path, pdfs)
        classifications = pdfFun.PDFclassifier(pageData)

        return classifications     

def classifyEverythingElse(path : Path) -> list[dict[str : str, str : str, str : str]]:
        pdfs, notPDFS = separatePDFs(path)
        classificatiions = generalClassifier(path, notPDFS)
        
        return classificatiions

def generalClassifier(path: Path, files: list[str]) -> list[dict[str, str]]:
        pageData = []
         
        for file in files:
                filePath = path / file
                fileExtension = Path(file).suffix.lower().lstrip(".")
                
                if fileExtension in ["docx", "pptx", "xlsx"]:
                        with zipfile.ZipFile(filePath, "r") as microsoftSuiteFile:
                                names = microsoftSuiteFile.namelist()

                                has_media = any(
                                name.startswith("word/media/") or
                                name.startswith("ppt/media/") or
                                name.startswith("xl/media/")
                                for name in names
                                )

                        pageData.append({
                                "file": file,
                                "file_type": fileExtension,
                                "text_type": "generalFile",
                                "content_type": "mixedFile" if has_media else "nativeFile"
                        })

                elif fileExtension in ["html", "htm", "xhtml", "xml"]:
                        content = filePath.read_text(encoding="utf-8", errors="ignore")

                        if fileExtension in ["html", "htm"]:
                                parsedContent = BeautifulSoup(content, "html.parser")
                                has_media = parsedContent.find("img") is not None
                        else:
                                parsedContent = BeautifulSoup(content, "xml")
                                has_media = parsedContent.find(["img", "image"]) is not None

                        pageData.append({
                                "file": file,
                                "file_type": fileExtension,
                                "text_type": "generalFile",
                                "content_type": "mixedFile" if has_media else "nativeFile"
                        })

                else:
                        pageData.append({
                                "file": file,
                                "file_type": fileExtension,
                                "text_type": "generalFile",
                                "content_type": "nativeFile"
                        })
        return pageData

def printFilesAndConfigurations(pdfClassification : list[dict[str : str, str : str, str : str]], not_pdfs : list[dict[str : str, str : str, str : str]]) -> None:
        allClassifications = [{"classification_group": "PDF",**pdf}
        for pdf in pdfClassification
        ] + [
        {
        "classification_group": "General",
        **general
        }
        for general in not_pdfs
        ]

        lines = [
        "=" * 50,
        f"File Classifications: {len(allClassifications)} total",
        f"PDF Classifications: {len(pdfClassification)}",
        f"General Classifications: {len(not_pdfs)}",
        "=" * 50,
        ]

        for index, item in enumerate(allClassifications, start=1):
                lines.append(
                f"{index:02d}. "
                f"[{item['classification_group']}] "
                f"{item['file']} | "
                f"type={item['file_type']} | "
                f"text={item['text_type']} | "
                f"content={item['content_type']}"
                )

        lines.append("=" * 50)

        logger.info("\n%s", "\n".join(lines))

def batchParserPlans(parserPlans : list[dict[str, str]]) -> dict[str, list[list[dict[str, Any]]]]:
        batches = {}
        batchSizes = {
                "doclingScannedOCR": 1,
                "doclingOCR": 2,
                "doclingNative": 8,
                "markerOCR": 12,
        }
        
        for item in parserPlans:
                parser = item["parser_plan"]
                parserBatchSize = batchSizes.get(parser, 1)

                parser_batches = batches.setdefault(parser, [])

                if not parser_batches or len(parser_batches[-1]) >= parserBatchSize:
                        parser_batches.append([])

                parser_batches[-1].append(item)

        return batches

def chooseParserPlan(pdfClassification : list[dict[str : str, str : str, str : str]], not_pdfs : list[dict[str : str, str : str, str : str]]) -> list[dict[str, str]]:
        parserPlans = []
        
        for pdf in pdfClassification:
                if pdf["content_type"] == "scientific" and (pdf["text_type"] == "scannedPDF" or pdf["text_type"] == "nativePDF"):
                        pdf["parser_plan"] = "markerOCR"

                if pdf["content_type"] == "scientific" and pdf["text_type"] == "mixedPDF":
                        pdf["parser_plan"] = "markerOCRPlusLLM"

                if pdf["content_type"] == "generic" and pdf["text_type"] == "mixedPDF":
                        pdf["parser_plan"] = "doclingOCR"

                if pdf["content_type"] == "generic" and pdf["text_type"] == "scannedPDF":
                        pdf["parser_plan"] = "doclingScannedOCR"
                
                if pdf["content_type"] == "generic" and pdf["text_type"] == "nativePDF":
                        pdf["parser_plan"] = "doclingNative"

                if pdf["content_type"] == "generic" and pdf["text_type"] == "unknown":
                        pdf["parser_plan"] = "doclingNative"

                parserPlans.append(pdf)
        
        for notPDF in not_pdfs:
                if notPDF["content_type"] == "mixedFile":
                        notPDF["parser_plan"] = "doclingOCR"
                
                if notPDF["content_type"] == "nativeFile":
                        notPDF["parser_plan"] = "doclingNative"
                
                parserPlans.append(notPDF)

        return parserPlans