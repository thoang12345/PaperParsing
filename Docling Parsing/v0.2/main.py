from Functions import functions as fun

fun.giveGPUstatus()
chunkingTools = fun.initializeDoclingChunker()

folders = ["Input", "Output", "ChromaDB"]
relativePaths = fun.buildRelativePaths(folders)

inputFolder = relativePaths[0]
outputFolder = relativePaths[1] 
chromaDBFolder = relativePaths[2]

PDFclassifications = fun.classifyPDFs(inputFolder)
generalClassifications = fun.classifyEverythingElse(inputFolder)

fun.printFilesAndConfigurations(PDFclassifications, generalClassifications)

client = fun.createChromaDBClient(chromaDBFolder)
fun.createOrDeleteChromaDBCollection(client)
fun.addToChromaDB(client)
fun.queryChromaDB(client)


doOrNotDoConvert = input("\nDo you want to convert files? (y/n): ").lower()

if doOrNotDoConvert == "y":
    markerResults = fun.convertPDFsMarker(PDFclassifications, generalClassifications, inputFolder, outputFolder)
    doclingResults = fun.convertDocumentsDocling(PDFclassifications, generalClassifications, inputFolder, outputFolder, chunkingTools)

output = fun.findOutputFiles(outputFolder, PDFclassifications, generalClassifications)    

print(output)