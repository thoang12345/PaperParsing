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
        specificPages = pageList(path, pdfs)
        
        for i, pdf in enumerate(pdfs):
                with fitz.open(path / pdf) as doc:
                        for pageNum in specificPages[i]:
                                page = doc[pageNum]
        
                                # 1. Count Words
                                # returns a list of tuples: (x0, y0, x1, y1, "word", block_no, line_no, word_no)
                                words_list = page.get_text("words")
                                word_count = len(words_list)
                                
                                # 2. Count Images
                                # returns a list of tuples containing image metadata and xref IDs
                                images_list = page.get_images(full=True)
                                image_count = len(images_list)

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