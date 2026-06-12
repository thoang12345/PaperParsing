from Functions import functions as fun

folders = ["Input", "Output"]
relativePaths = fun.buildRelativePaths(folders)

inputFolder = relativePaths[0]
outputFolder = relativePaths[1] 

classifications, not_pdfs = fun.classifyPDFs(inputFolder)
parserplans = fun.chooseParserPlan(classifications, not_pdfs)

print(parserplans)


