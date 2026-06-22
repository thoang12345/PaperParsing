from Functions import functions as fun

folders = ["Input", "Output"]
relativePaths = fun.buildRelativePaths(folders)

inputFolder = relativePaths[0]
outputFolder = relativePaths[1] 

PDFclassifications = fun.classifyPDFs(inputFolder)
generalClassifications = fun.classifyEverythingElse(inputFolder)

results = fun.convertPDFsDocling(PDFclassifications, generalClassifications, inputFolder)

for parser_result in results:
        parser_name = parser_result["name"]
        conversion_generator = parser_result["result"]
        batch = parser_result["batch"]
           
        print(f"\nResults from {parser_name}")

        for i, conversion_result in enumerate(conversion_generator):
                markdown = conversion_result.document.export_to_markdown()

                print(f"document {batch[i]["file"]}\n")
                print(markdown[:100])