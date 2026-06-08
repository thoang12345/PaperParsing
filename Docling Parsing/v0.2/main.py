import functions as fun

folders = ["Input", "Output"]
relativePaths = fun.buildRelativePaths(folders)

inputFolder = relativePaths[0]
outputFolder = relativePaths[1] 

pages = fun.classifyPDFs(inputFolder)

print(type((pages[0])[1]))