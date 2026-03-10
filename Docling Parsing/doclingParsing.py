import functions as fun
import time

fun.clear_terminal()
start = time.time()

lePath = r"D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Epstein Files\Motor Skid"
lePaperPath = r"D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Epstein Files\Papers"
outputPath = r"D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output"
outputPathMotor = r"D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output Motor Skid"

gimmeFileNames = fun.gimmeFileNames(lePath)
file_paths = fun.buildFilePaths(lePath)
addElements = True

pipelineOptions = fun.pipelineOptions(ImageScale=6.9444444444,
                                      generatePictureImages=addElements,
                                      doFormulas=addElements,
                                      doOcr = True)

for i, file in enumerate(file_paths):
    convertedFile = fun.convertFile(file, pipelineOptions)
    fun.writeItDown(convertedFile, outputPathMotor, gimmeFileNames[i], addElements)
    fun.returnFormulas(outputPathMotor, gimmeFileNames[i], convertedFile)

end = time.time()

fun.printRunStats(lePath, outputPathMotor, start, end)