from Functions import functions as fun

fun.giveGPUstatus()

folders = ["Input", "Output"]
relativePaths = fun.buildRelativePaths(folders)

inputFolder = relativePaths[0]
outputFolder = relativePaths[1] 

PDFclassifications = fun.classifyPDFs(inputFolder)
generalClassifications = fun.classifyEverythingElse(inputFolder)

markerResults = fun.convertPDFsMarker(PDFclassifications, generalClassifications, inputFolder, outputFolder)
doclingResults = fun.convertDocumentsDocling(PDFclassifications, generalClassifications, inputFolder, outputFolder)

