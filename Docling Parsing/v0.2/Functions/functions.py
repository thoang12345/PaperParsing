from pathlib import Path
import zipfile
from bs4 import BeautifulSoup
from Functions import functionsClassify as pdfFun
from dataclasses import dataclass

def buildRelativePaths(paths : list[str]) -> list[Path]:
        relativePath = Path(__file__).parent.parent
        buildRelativePaths = [relativePath / path for path in paths]
        
        return buildRelativePaths

def parseFiles(path : Path) -> list[str]:
        fileNames = [file.name for file in path.iterdir() if file.is_file()]
        
        return fileNames

def filterPDFs(path : Path) -> list[str]:
        files = parseFiles(path)
        PDFFiles = [pdf for pdf in files if pdf.endswith(".pdf")]
        
        return PDFFiles

def separatePDFs(path : Path) -> tuple[list[Path], list[Path]]:
        files = parseFiles(path)
        pdfs = filterPDFs(path)
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

def chooseParserPlan(pdfClassification : list[dict[str : str, str : str, str : str]], not_pdfs : list[dict[str : str, str : str, str : str]]) -> list[dict[str, str]]:
        parserPlans = []
        
        for pdf in pdfClassification:
                if pdf["content_type"] == "scientific" and pdf["text_type"] == "mixedPDF":
                        pdf["parser_plan"] = "markerOCR"

                if pdf["content_type"] == "generic" and pdf["text_type"] == "mixedPDF":
                        pdf["parser_plan"] = "doclingOCR"

                if pdf["content_type"] == "generic" and pdf["text_type"] == "scannedPDF":
                        pdf["parser_plan"] = "doclingOCR"
                
                if pdf["content_type"] == "generic" and pdf["text_type"] == "nativePDF":
                        pdf["parser_plan"] = "doclingNative"
                        
                parserPlans.append(pdf)
        
        for notPDF in not_pdfs:
                if notPDF["content_type"] == "mixedFile":
                        notPDF["parser_plan"] = "generalOCR"
                
                if notPDF["content_type"] == "nativeFile":
                        notPDF["parser_plan"] = "generalNoOCR"
                
                parserPlans.append(notPDF)

        return parserPlans

def choosingParserSettings(pdfClassifications : list[dict[str : str, str : str, str : str]], generalClassifications : list[dict[str : str, str : str, str : str]]) -> str:
        parserPlans = chooseParserPlan(pdfClassifications, generalClassifications)

@dataclass(frozen=True)
class doclingPipelineOptions:
        
        #image / visual assets 
        imageScale : float = 1.0
        generatePictureImages : bool = False
        generatePageImage : bool = False
        
        #bum ahh OCR
        doOCR : bool = False
        forceFullPageOCR : bool = False
        
        
        

def doclingSettings(pdfClassifications : list[dict[str : str, str : str, str : str]], generalClassifications : list[dict[str : str, str : str, str : str]]):
        ...

def markerSettings(pdfClassifications : list[dict[str : str, str : str, str : str]], generalClassifications : list[dict[str : str, str : str, str : str]]):
        ...






