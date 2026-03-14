import functions as fun
import time
from dataclasses import dataclass

start = time.time()

lePath = r"D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Epstein Files\Motor Skid"
lePaperPath = r"D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Epstein Files\Papers"
outputPath = r"D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output"
outputPathMotor = r"D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output Motor Skid"

gimmeFileNames = fun.gimmeFileNames(lePath)
file_paths = fun.buildFilePaths(lePath)

# Set the options for the pipeline
@dataclass
class PipelineConfig:
    addElements: bool = True
    ImageScale: float = 7
    doOcr: bool = True
    tableStructure: bool = True
    ocrBatchSize: int = 32
    layoutBatchSize: int = 32
    tableBatchSize: int = 4
    
config = PipelineConfig()
pipelineOptions = fun.initializeStuff(config)

for i, file in enumerate(file_paths):
    convertedFile = fun.convertFile(file, gimmeFileNames[i], pipelineOptions)
    fun.writeItDown(convertedFile, outputPathMotor, gimmeFileNames[i], config.addElements)
    fun.returnFormulas(outputPathMotor, gimmeFileNames[i], file, convertedFile)

end = time.time()

fun.printRunStats(lePath, outputPathMotor, start, end, config)