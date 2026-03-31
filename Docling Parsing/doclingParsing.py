import functions as fun
import time
from dataclasses import dataclass

start = time.time()

lePath = r"F:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Epstein Files\Motor Skid"
lePaperPath = r"F:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Epstein Files\Papers"
outputPath = r"F:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output"
outputPathMotor = r"F:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output Motor Skid"
document = r"F:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output.md"

chosenPath = lePath
chosenOutputPath = outputPathMotor

gimmeFileNames = fun.gimmeFileNames(chosenPath)
file_paths = fun.buildFilePaths(chosenPath)

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
chunker, tokenizer = fun.intitChunker()
Parse = False
pipelineOptions = fun.initializeStuff(config)

for i, file in enumerate(file_paths):
    convertedFile = fun.convertFile(file, gimmeFileNames[i], pipelineOptions)
    fun.writeItDown(convertedFile, chosenOutputPath, gimmeFileNames[i], config.addElements)
    fun.writeChunksDown(chosenOutputPath, chosenOutputPath, gimmeFileNames[i])

end = time.time()

fun.printRunStats(chosenPath, chosenOutputPath, start, end, config)
