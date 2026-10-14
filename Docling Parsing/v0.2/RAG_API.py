import os
from pathlib import Path
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

client = chroma.createChromaDBClient(chromaDBFolder)


def rag_api(input_path: Path, collection_name: str, profile_name: str):
    pdfClassifications = classify.classifyPDFs(input_path)
    generalClassifications = classify.classifyEverythingElse(input_path)

    parserPlans = classify.chooseParserPlan(pdfClassifications, generalClassifications)
    parserPlans.sort(key=lambda plan: plan["parser_plan"])

    marker.convertDocumentsMarker(
            parserPlans,
            input_path,
            outputFolder
        )
    
    docling.convertDocumentsDocling(
        parserPlans,
        input_path,
        outputFolder
    )

    chunkOutput = chunking.chunkDocuments(outputFolder, pdfClassifications, generalClassifications, chunkingTools)    
    
    chroma.addToChromaDB(client, collection_name=collection_name, profile_name=profile_name, inputChunks=chunkOutput)

rag_api(input_path=Path("/home/thienan/Documents/GitHub/PaperParsing/Docling Parsing/v0.2/Input"), collection_name="test2", profile_name="doclingNative")
