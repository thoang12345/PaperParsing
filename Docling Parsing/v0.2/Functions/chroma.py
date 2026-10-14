import chromadb
from pathlib import Path
from Functions import utilities
from Functions.utilities import logger, t
import os

def createChromaDBClient(chromaDBFolder: Path) -> chromadb.api.client.Client:
        client = chromadb.PersistentClient(path=str(chromaDBFolder))
        return client

def getChromaDBCollections(client: chromadb.api.client.Client) -> chromadb.api.models.Collection:
        collections = client.list_collections()
        return collections

def deleteChromaDBCollection(client: chromadb.api.client.Client, collection_name: str) -> None:
        collections = getChromaDBCollections(client)
        collectionNames = [col.name for col in collections]

        if collection_name in collectionNames:
                client.delete_collection(name=collection_name)
        else:
                return                

def createChromaDBCollection(client: chromadb.api.client.Client, collection_name: str, description: str) -> None:  
        if len(collection_name) < 3 or len(collection_name) > 512:
                return 

        if not (bool(collection_name and collection_name[0].isalnum() and collection_name[-1].isalnum())):
                return

        passed_name = collection_name.lower().replace(" ", "-")
              
        collections = client.create_collection(
                name=passed_name,
                metadata={"description": description, "hnsw:space": "cosine"},
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
    
def addToChromaDB(client: chromadb.api.client.Client, collection_name: str, profile_name: str, inputChunks : dict[str, list]) -> None:
        collections = getChromaDBCollections(client)
        collectionNames = [col.name for col in collections]

        if collection_name not in collectionNames:
                return

        document_chunks = inputChunks[profile_name]

        collection = client.get_collection(name=collection_name)

        for chunk in document_chunks:
                name = chunk["name"]
                chunks = chunk["chunks"]
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
                                        "chunk number": metadata["chunkNumber"] or "None",
                                        "picture description": metadata["pictureDescription"] or "None",
                                        "profile_name": profile_name
                                }],
                        )

                        logger.info(f"Added chunk {chunkNumber + 1} of {len(chunks)} to {collection_name}")

