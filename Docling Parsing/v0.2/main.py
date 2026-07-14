from Functions import functions as fun

fun.giveGPUstatus()
chunkingTools = fun.initializeDoclingChunker()

folders = ["Input", "Output", "ChromaDB"]
relativePaths = fun.buildRelativePaths(folders)

inputFolder = relativePaths[0]
outputFolder = relativePaths[1] 
chromaDBFolder = relativePaths[2]

client = fun.createChromaDBClient(chromaDBFolder)
PDFclassifications = fun.classifyPDFs(inputFolder)
generalClassifications = fun.classifyEverythingElse(inputFolder)

fun.printFilesAndConfigurations(PDFclassifications, generalClassifications)

fun.createOrDeleteChromaDBCollection(client)

fun.queryChromaDB(client)

doOrNotDoConvert = input("\nDo you want to cc;convert files? (y/n): ").lower()
print("\n")

if doOrNotDoConvert == "y":
    markerResults = fun.convertPDFsMarker(PDFclassifications, generalClassifications, inputFolder, outputFolder)
    doclingResults = fun.convertDocumentsDocling(PDFclassifications, generalClassifications, inputFolder, outputFolder, chunkingTools)

chunkOutput = fun.chunkDocuments(outputFolder, PDFclassifications, generalClassifications, chunkingTools)    

fun.addToChromaDB(client, chunkOutput)