import functions as fun
import time
from dataclasses import dataclass

startAll = time.time()

lePath = r"D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Epstein Files\Motor Skid"
lePaperPath = r"D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Epstein Files\Papers"
outputPath = r"D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output"
outputPathMotor = r"D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output Motor Skid"
document = r"D:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output\acoustics-08-00006-v2\acoustics-08-00006-v2_output.md"

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
    allowExternalPlugins: bool = True
    doPictureDescriptions: bool = False
    pictureDescriptionPrompt: str = "Describe the image in 2-3 sentences. Be concise and accurate. No markdown syntax."
    
    
config = PipelineConfig()
converter, generator, tokenizer = fun.initializeStuff(config)

BATCH_SIZE = 8
results = []

parsedPaths, parsedNames, numParsed = fun.filterParsed(file_paths, names, chosenOutputPath)

for i in range(0, len(parsedPaths), BATCH_SIZE):
    batch_paths = parsedPaths[i:i+BATCH_SIZE]
    batch_names = parsedNames[i:i+BATCH_SIZE]

    results = fun.convertFile(batch_paths, batch_names, converter)

    for j, result in enumerate(results):
        fun.writeItDown(result, chosenOutputPath, batch_names[j], config.addElements)

    batchDocuments = [result.document for result in results]

    allChunks = []
    allPrompts = []
    chunkCounts = []
    allStartTimes = []

    for docIdx, name in enumerate(batch_names):
        chunks, startTime, prompts = fun.chunkDocument(chosenOutputPath, name)
        allChunks.append(chunks)
        allStartTimes.append(startTime)
        allPrompts.append(prompts)
        chunkCounts.append(len(chunks))

    flatPrompts = [p for prompts in allPrompts for p in prompts]
    print(f"\nGenerating summaries for {len(flatPrompts)} chunks across {len(batch_names)} files...\n")
    flatSummaries = generator(flatPrompts, truncation=True, return_full_text=False, batch_size=8)

    summaryIdx = 0
    for k, name in enumerate(batch_names):
        count = chunkCounts[k]
        fileSummaries = flatSummaries[summaryIdx:summaryIdx+count]
        filePrompts = allPrompts[k]
        fun.writeChunksDown(allChunks[k], fileSummaries, filePrompts, chosenOutputPath, name, allStartTimes[k])
        summaryIdx += count
        
endAll = time.time()

fun.printRunStats(startAll, endAll, config, numParsed, len(results))
