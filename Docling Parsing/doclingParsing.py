import functions as fun
import time

fun.clear_terminal()
start = time.time()

lePath = r"C:\Users\mayhe\OneDrive\Documents\PaperParsing\Docling Parsing\Epstein Files\Motor Skid"
lePaperPath = r"C:\Users\mayhe\OneDrive\Documents\PaperParsing\Docling Parsing\Epstein Files\Papers"
outputPath = r"C:\Users\mayhe\OneDrive\Documents\PaperParsing\Docling Parsing\Output"

gimmeFileNames = fun.gimmeFileNames(lePaperPath)
file_paths = fun.buildFilePaths(lePaperPath)
addElements = True

pipelineOptions = fun.pipelineOptions(ImageScale=6.9444444444,
                                      generatePictureImages=addElements,
                                      doFormulas=addElements,
                                      doOcr = True)

for i, file in enumerate(file_paths):
    convertedFile = fun.convertFile(file, pipelineOptions)
    fun.writeItDown(convertedFile, outputPath, gimmeFileNames[i], addElements)
    fun.returnFormulas(outputPath, gimmeFileNames[i], convertedFile)

end = time.time()

fun.printRunStats(lePaperPath, outputPath, start, end)