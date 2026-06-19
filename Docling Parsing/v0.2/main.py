from Functions import functions as fun

folders = ["Input", "Output"]
relativePaths = fun.buildRelativePaths(folders)

inputFolder = relativePaths[0]
outputFolder = relativePaths[1] 

PDFclassifications = fun.classifyPDFs(inputFolder)
generalClassifications = fun.classifyEverythingElse(inputFolder)

sortedParserPlans = fun.convertPDFsDocling(PDFclassifications, generalClassifications)

print(sortedParserPlans)
