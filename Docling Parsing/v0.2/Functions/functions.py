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

def classifyPDFs(path : Path) -> dict[str : str]:
        pdfs, not_pdfs = separatePDFs(path)
        pageData = pdfFun.extractPageData(path, pdfs)
        classifications = pdfFun.classify(pageData)

        return classifications       













