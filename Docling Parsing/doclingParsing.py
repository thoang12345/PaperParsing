import functions as fun
import time
from dataclasses import dataclass

startAll = time.time()

lePath = r"D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Epstein Files\Motor Skid"
lePaperPath = r"D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Epstein Files\Papers"
outputPath = r"D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output"
outputPathMotor = r"D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output Motor Skid"
document = r"D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output.md"

chosenPath = lePaperPath
chosenOutputPath = outputPath
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
    allowExternalPlugins: bool = True
    doPictureDescriptions: bool = False
    pictureDescriptionPrompt: str = "Describe the image in 2-3 sentences. Be concise and accurate. No markdown syntax."
    
config = PipelineConfig()
converter, generator, tokenizer, databaseClient, theMass = fun.initializeStuff(config)

BATCH_SIZE = 8
results = []

parsedPaths, parsedNames, numParsed = fun.filterParsed(file_paths[0:50], names[0:50], theMass)

fun.batchInjection(parsedPaths, parsedNames, converter, BATCH_SIZE, config, chosenOutputPath, generator, tokenizer, theMass)
    
    
endAll = time.time()

fun.printRunStats(startAll, endAll, config, numParsed, len(results))


'''
To DO:
Get ChromaDB working
Try different query methods (Chunk only/metadata only/both/specific metadata like the summary/HNSW (Hierarchical Navigable Small World))
    - Log CPU utilization, Ram, time, correctness/accuracy 

Look into ticktock for time stuff lol

'''

