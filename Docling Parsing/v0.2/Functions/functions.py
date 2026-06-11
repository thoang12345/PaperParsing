from pathlib import Path
from Functions import functionsPDF as pdfFun

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
        not_pdfs = [pdf for pdf in files if not pdf.endswith(".pdf")]
        
        return pdfs, not_pdfs

def classifyPDFs(path : Path) -> list[dict[str : str, str : str, str : str]]:
        pdfs, not_pdfs = separatePDFs(path)
        pageData = pdfFun.extractPageData(path, pdfs)
        classifications = pdfFun.classify(pageData)

        return classifications, not_pdfs       

def chooseParserPlan(classification : list[dict[str : str, str : str, str : str]], not_pdfs : list[str]) -> str:
        for pdf in classification:
                if pdf["content_type"] == "scientific" and pdf["text_type"] == "mixedPDF":
                        pdf["parser_plan"] = "markerOCR"

                if pdf["content_type"] == "generic" and pdf["text_type"] == "mixedPDF":
                        pdf["parser_plan"] = "doclingOCR"

                if pdf["content_type"] == "generic" and pdf["text_type"] == "scannedPDF":
                        pdf["parser_plan"] = "doclingOCR"
                
                if pdf["content_type"] == "generic" and pdf["text_type"] == "nativePDF":
                        pdf["parser_plan"] = "doclingNative"
        
        for notPDF in not_pdfs:
                notPDFDict = {"file_name" : notPDF, "content_type" : "notPDF", "text_type" : "notPDF", "parser_plan" : "notPDF"}
                classification.append(notPDFDict)

        return classification






