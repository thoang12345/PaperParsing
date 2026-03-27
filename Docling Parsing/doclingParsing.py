import functions as fun
import time
from dataclasses import dataclass

start = time.time()

lePath = r"F:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Epstein Files\Motor Skid"
lePaperPath = r"F:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Epstein Files\Papers"
outputPath = r"F:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output"
outputPathMotor = r"F:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output Motor Skid"
document = r"F:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output.md"

chosenPath = lePaperPath
chosenOutputPath = outputPath

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
<<<<<<< Updated upstream
pipelineOptions = fun.initializeStuff(config)
=======
chunker, tokenizer = fun.intitChunker()
Parse = False

pix2texModel, pipelineOptions = fun.initializeStuff(config)
>>>>>>> Stashed changes

for i, file in enumerate(file_paths[0:5]):
    convertedFile = fun.convertFile(file, gimmeFileNames[i], pipelineOptions)
<<<<<<< Updated upstream
    fun.writeItDown(convertedFile, outputPathMotor, gimmeFileNames[i], config.addElements)
    fun.returnFormulas(outputPathMotor, gimmeFileNames[i], file, convertedFile)
=======
    fun.chunkDocument(convertedFile, chunker, tokenizer, gimmeFileNames[i], chosenOutputPath)
    fun.writeItDown(convertedFile, chosenOutputPath, gimmeFileNames[i], config.addElements)
    #fun.returnFormulas(pix2texModel, chosenOutputPath, gimmeFileNames[i], convertedFile)
>>>>>>> Stashed changes

end = time.time()

fun.printRunStats(chosenPath, chosenOutputPath, start, end, config)