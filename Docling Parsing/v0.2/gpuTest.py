from docling.document_converter import DocumentConverter

converter = DocumentConverter()
result = converter.convert("/home/thienan/Documents/Github/PaperParsing/Docling Parsing/v0.2/Input/MA #4 Academic Research with Essay Thienan Hoang.docx")

print(result.document.export_to_markdown())