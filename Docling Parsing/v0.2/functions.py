from pathlib import Path
import fitz
import random

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
        pageData = extractPageData(path, pdfs)
        classifications = classify(pageData)

        return classifications
                                        
def extractPageData(path: Path, pdfs: list[str]) -> list[dict[str, str | list[dict[str, int]]]]:
        specificPages = pageList(path, pdfs)
        pageData = []

        for i, pdf in enumerate(pdfs):
                with fitz.open(path / pdf) as doc:
                        pages = [
                        {
                                "page_number": p.number + 1,
                                "words": len(p.get_text("words")),
                                "images": len(p.get_images(full=True)),
                        }
                        for pageNum in specificPages[i]
                        for p in [doc[pageNum]]  # Assignment trick to avoid repeating doc[pageNum]
                        ]

                pageData.append({
                "file": pdf,
                "pages": pages,
        })        

        return pageData          
           
def countPages(path : Path, pdfs : list[str]) -> list[int]:
        pageNumber = []
        for pdf in (pdfs):
                with fitz.open(path / pdf) as doc:
                        pageNumber.append(doc.page_count)
        return pageNumber                        
                
def pageList(path : Path, pdfs : list[str]) -> list[list[int]]:
        listPageNumbers = countPages(path, pdfs)
        specificPages = []
        for pageNumber in listPageNumbers:
                middle = (pageNumber + 1) // 2
                if pageNumber < 4:
                        specificPages.append([0, -1, middle])
                elif pageNumber > 5 and pageNumber < 11:
                        specificPages.append([0, 1, -1, -2, middle])
                else:
                        specificPages.append([0, 1, -1, -2, middle, middle - 1, random.randint(2, middle - 2), random.randint(2, middle - 2), random. randint(middle + 1, pageNumber - 3), random. randint(middle + 1, pageNumber - 3)])
        return specificPages        

def classify(pageDataPDFs : list[dict[str, str | list[dict[str, int]]]]) -> list[str]:
        results = []

        for pdf in pageDataPDFs:

                fileName = pdf["file"]
                pages = pdf["pages"]
                print((pages))
                features = summarizePDFPages(pages)
        
        return features

def summarizePDFPages(pages : list[dict[str, int]]) -> list[int]:
        totalWords = 0
        totalImages = 0
        pageCount = len(pages)
        maxWordsOnPage = 0
        imageHeavyPages = 0

        for page in pages:
                totalWords += page["words"]
                totalImages += page["images"]

                if page["words"] > maxWordsOnPage:
                        maxWordsOnPage = page["words"]

                if page["images"] > page["words"]:
                        imageHeavyPages += 1

        return [totalWords, totalImages, pageCount, maxWordsOnPage, imageHeavyPages]

def classifyTextType(features : list[int]) -> str:
        totalWords = features[0]
        totalImages = features[1]
        pageCount = features[2]
        maxWordsOnPage = features[3]
        imageHeavyPages = features[4]
        
        if totalWords < totalImages:
                return "scannedPDF"
        
        


