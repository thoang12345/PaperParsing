from Functions import classify
from pathlib import Path

def buildRelativePaths(paths : list[str]) -> list[Path]:
        relativePath = Path(__file__).parent.parent
        buildRelativePaths = [relativePath / path for path in paths]
        
        return buildRelativePaths

def parseFiles(path : Path) -> list[str]:
        fileNames = [file.name for file in path.iterdir() if file.is_file() and "Zone.Identifier" not in file.name]
        
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

def findOutputFiles(outputFolder: Path, 
                    pdfClassification : list[dict[str : str, str : str, str : str]], 
                    not_pdfs : list[dict[str : str, str : str, str : str]]
                    ) -> list[dict[str, str | dict[str, Path]]]:
        parserPlans = classify.chooseParserPlan(pdfClassification, not_pdfs)
        sortedParserPlans = sorted(parserPlans, key=lambda x: x["parser_plan"])
        
        names = [Path(entry["file"]).stem for entry in sortedParserPlans]

        for i, name in enumerate(names):
                sortedParserPlans[i]["output"] = findMarkdownJSON(outputFolder, name)

        return sortedParserPlans

def findMarkdownJSON(outputFolder : Path, name : str) -> dict[str : Path]:
        #path = [path for path in outputFolder.rglob("*") if path.is_file() and path.suffix.lower() in {".md", ".json"} and name.lower() in path.name.lower()]

        markdown_file = next(outputFolder.rglob(f"{name}.md"), None)
        json_file = next(outputFolder.rglob(f"{name}.json"), None)

        return {"markdown" : markdown_file, "JSON" : json_file}