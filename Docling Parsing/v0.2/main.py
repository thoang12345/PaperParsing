import os
os.environ["MIOPEN_CONV_PRECISE_ROCBLAS_TIMING"] = "0"
os.environ["MIOPEN_FIND_MODE"] = "2"
os.environ["MIOPEN_LOG_LEVEL"] = "2"
os.environ["HSA_ENABLE_SDMA"] = "0"
os.environ["HSA_OVERRIDE_GFX_VERSION"] = "11.5.0"  # ← this is the missing piece
os.environ["TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL"] = "1"
from Functions import system
from Functions import classify
from Functions import paths
from Functions import doclingParser as docling
from Functions import markerParser as marker
from Functions import llm
from Functions import chunking
from Functions import chroma
from Functions import query

system.giveGPUstatus()
chunkingTools = system.initializeDoclingChunker()

folders = ["Input", "Output", "ChromaDB"]
relativePaths = paths.buildRelativePaths(folders)

inputFolder = relativePaths[0]
outputFolder = relativePaths[1] 
chromaDBFolder = relativePaths[2]

print(chromaDBFolder)

client = chroma.createChromaDBClient(chromaDBFolder)
pdfClassifications = classify.classifyPDFs(inputFolder)
generalClassifications = classify.classifyEverythingElse(inputFolder)

parserPlans = classify.chooseParserPlan(
        pdfClassifications,
        generalClassifications
    )

parserPlans.sort(key=lambda plan: plan["parser_plan"])

batches = classify.batchParserPlans(parserPlans)

classify.printFilesAndConfigurations(pdfClassifications, generalClassifications)

chroma.createOrDeleteChromaDBCollection(client)

query.queryChromaDB(client)

doOrNotDoConvert = input("\nDo you want to convert files? (y/n): ").lower()
print("\n")

if doOrNotDoConvert == "y":
    marker.convertDocumentsMarker(
        parserPlans,
        inputFolder,
        outputFolder
    )

    docling.convertDocumentsDocling(
        parserPlans,
        inputFolder,
        outputFolder
    )

doOrNotDoConvert = input("\nDo you want to chunk files? (y/n): ").lower()

if doOrNotDoConvert == "y":
    generator = llm.initializeTransformer()
    chunkOutput = chunking.chunkDocuments(outputFolder, pdfClassifications, generalClassifications, chunkingTools)    

    chroma.addToChromaDB(client, chunkOutput)