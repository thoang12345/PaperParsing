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

client = chroma.createChromaDBClient(chromaDBFolder)
PDFclassifications = classify.classifyPDFs(inputFolder)
generalClassifications = classify.classifyEverythingElse(inputFolder)

classify.printFilesAndConfigurations(PDFclassifications, generalClassifications)

chroma.createOrDeleteChromaDBCollection(client)

query.queryChromaDB(client)

doOrNotDoConvert = input("\nDo you want to convert files? (y/n): ").lower()
print("\n")

if doOrNotDoConvert == "y":
    markerResults = marker.convertPDFsMarker(PDFclassifications, generalClassifications, inputFolder, outputFolder)
    doclingResults = docling.convertDocumentsDocling(PDFclassifications, generalClassifications, inputFolder, outputFolder, chunkingTools)

generator = llm.initializeTransformer()
chunkOutput = chunking.chunkDocuments(outputFolder, PDFclassifications, generalClassifications, chunkingTools, generator)    

chroma.addToChromaDB(client, chunkOutput)