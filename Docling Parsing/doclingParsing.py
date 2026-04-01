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

names = fun.gimmeFileNames(chosenPath)
file_paths = fun.buildFilePaths(chosenPath)

# Set the options for the pipeline
@dataclass
class PipelineConfig:
    addElements: bool = True
    ImageScale: float = 2.7
    doOcr: bool = True
    tableStructure: bool = True
    ocrBatchSize: int = 32
    layoutBatchSize: int = 32
    tableBatchSize: int = 4
    
config = PipelineConfig()
chunker, tokenizer = fun.intitChunker()
Parse = False
converter = fun.initializeStuff(config)

BATCH_SIZE = 5

for i in range(0, len(file_paths), BATCH_SIZE):
    batch_paths = file_paths[i:i+BATCH_SIZE]
    batch_names = names[i:i+BATCH_SIZE]

    results = fun.convertFile(batch_paths, batch_names, converter)

    for j, result in enumerate(results):
        fun.writeItDown(result, chosenOutputPath, batch_names[j], config.addElements)
        fun.writeChunksDown(chosenOutputPath, chosenOutputPath, batch_names[j])

end = time.time()

fun.printRunStats(chosenPath, chosenOutputPath, start, end, config)
