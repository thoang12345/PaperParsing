from pathlib import Path
import functionsPDF as pdfFun

def buildRelativePaths(paths : list[str]) -> list[Path]:
        relativePath = Path(__file__).parent
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
        classifications = classify(pageData)

        return classifications       

def classify(pageDataPDFs: list[dict[str, str | list[dict[str, int]]]]) -> list[dict[str, str]]:
    results = []

    for pdf in pageDataPDFs:
        fileName = pdf["file"]
        pages = pdf["pages"]
        text = pdf["text"]

        features = pdfFun.build_content_features(text=text, pages=pages)
        textType = pdfFun.classifyTextType(features)
        contentDetails = pdfFun.classify_content_type_details(features)
        
        contentType = contentDetails["content_type"]

        results.append({
            "file": fileName,
            "text_type": textType,
            "content_type": contentType,
        })

    return results











