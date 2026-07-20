import chromadb
from pathlib import Path
from Functions import utilities
from Functions.utilities import logger, t
import os

def createChromaDBClient(chromaDBFolder: Path) -> chromadb.api.client.Client:
        client = chromadb.PersistentClient(path=str(chromaDBFolder))
        return client

def createOrDeleteChromaDBCollection(client: chromadb.api.client.Client) -> None:
        quit = True

        while quit:
                collections = getChromaDBCollections(client)

                if collections == []:
                        answerForCollections = utilities.getResponseFromUser(
                                "\nNo existing collections found. Would you like to create a new collection? (y/n): ",
                                ["y", "n"]
                        )
                else: 
                        answerForCollections = utilities.getResponseFromUser(
                                "\nExisting collections found. Would you like to create a new collection? (y/n). Or 'd' to delete an existing collection: ",
                                ["y", "n"]
                        )
                if answerForCollections == "quit":
                        quit = False
                        return
                if answerForCollections == "d":
                        deleteChromaDBCollection(client)

                if answerForCollections == "y":
                        createChromaDBCollection(client)

def getChromaDBCollections(client: chromadb.api.client.Client) -> chromadb.api.models.Collection:
        collections = client.list_collections()
        return collections

def deleteChromaDBCollection(client: chromadb.api.client.Client) -> None:
        collections = getChromaDBCollections(client)
        collectionNames = [col.name for col in collections]
        logger.info(f"Existing collections: {', '.join(collectionNames)}")

        quit = True
        while quit:
                collectionToDelete = utilities.getResponseFromUser(
                        f"Enter the name of the collection you want to delete. Or 'q' to quit:\nList of collections:\n {'\n'.join(collectionNames)}\n",
                        ["q"] + collectionNames
                )

                if collectionToDelete == 'quit':
                        quit = False        
                        break
                if collectionToDelete in collectionNames:
                        client.delete_collection(name=collectionToDelete)
                        logger.info(f"Collection '{collectionToDelete}' deleted successfully.")
                else:
                        logger.info(f"Collection '{collectionToDelete}' not found.")
                        continue

def createChromaDBCollection(client: chromadb.api.client.Client) -> None:
        collections = []
        
        quit = True
        while quit:
                createCollectionName = utilities.getResponseFromUser(
                        "Enter the name for the new collection or 'q' to quit: "
                )
        
                if createCollectionName == 'quit':
                        quit = False
                        return
                
                collectionDescription = input("Enter a description for the new collection (optional; leave blank if unwanted): ")
                collections = client.create_collection(
                        name=createCollectionName,
                        metadata={"description": collectionDescription, "hnsw:space": "cosine"},
                        configuration = {
                                "hnsw": {
                                        "space": "cosine",
                                        "ef_construction": 1000,
                                        "ef_search": 1000,
                                        "max_neighbors": 64,
                                        "num_threads": os.cpu_count(),
                                        "batch_size": 100,
                                        "sync_threshold": 1000,
                                        "resize_factor": 1.2,
                                }
                        }
                )
                logger.info(f"Collection '{createCollectionName}' created successfully.")
    
def addToChromaDB(client: chromadb.api.client.Client, inputChunks : dict[str, list]) -> None:
    collections = getChromaDBCollections(client)
    collectionNames = [col.name for col in collections]

    quit = True
    addToChromaOrNo = utilities.getResponseFromUser(
            f"\nDo you want to add documents to an existing collection? (y/n): ",
            ["y", "n"]
            )

    if addToChromaOrNo == "quit":
            return

    keysList = list(inputChunks)
    pickProfileToAdd = utilities.getResponseFromUser(
            f"Found profiles {', '.join(keysList)}. Pick one to ingest. Or 'q' to quit: ",
            keysList + ["q"]
    )

    if pickProfileToAdd == "quit":
            return
    
    documentChunks = inputChunks[pickProfileToAdd]
    logger.info(f"Found {len(documentChunks)} documents in {pickProfileToAdd}")

    addDocumentsYorN = utilities.getResponseFromUser(
            f"Do you want to add {pickProfileToAdd} documents to chroma? (y/n): ",
            ["y", "n"]
    )

    if addDocumentsYorN == "quit":
            return

    selectedCollection = utilities.getResponseFromUser(
            f"\nSelect a collection from existing ones to add documents to. Or 'q' to quit:\nList of collections:\n {'\n'.join(collectionNames)}\n",
            ["q"] + collectionNames
    )

    if selectedCollection == 'quit':
            return
    
    collection = client.get_collection(name = selectedCollection)

    for document in documentChunks:
            name = document["name"]
            chunks = document["chunks"]
            for chunkNumber, chunk in enumerate(chunks):
                    text = chunk["text"]
                    metadata = chunk["metadata"]

                    collection.add(
                            ids = f"{name}_chunkNumber_{chunkNumber}",
                            documents = [text],
                            metadatas = [{
                                    "document name": metadata["paperName"] or "None",
                                    "heading": metadata["headings"] or "None",
                                    "page numbers": metadata["pageNumbers"] or "None",
                                    "classifications": metadata["classifications"] or "None",
                                    "token count": metadata["tokenCount"] or "None",
                                    "contextualize": metadata["contextualize"] or "None",
                                    "chunk number": metadata["chunkNumber"] or "None"
                            }],
                    )

                    logger.info(f"Added chunk {chunkNumber} of {len(chunks)} to {selectedCollection}")