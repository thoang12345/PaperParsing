from Functions import chroma
from Functions.utilities import logger, t, getResponseFromUser

import chromadb

def queryChromaDB(client: chromadb.api.client.Client) -> None:
        collections = chroma.getChromaDBCollections(client)
        collectionNames = [col.name for col in collections]

        quit = True
        yesOrNoQuery = getResponseFromUser(
                f"\nDo you want to query an existing collection? (y/n): ".lower(), 
                ["y", "n"]
        )

        if yesOrNoQuery == "quit":
                return 

        getCollection = getResponseFromUser(
                f"\nSelect a collection from existing ones to query: {', '.join(collectionNames)}. Or 'q' to quit: ",
                collectionNames
        )
        
        if getCollection == "quit":
                return 

        collection = client.get_collection(name=getCollection)
        logger.info(f"Successfully found collection '{collection.name}'. You can now query this collection.")
        while quit:
                query = getResponseFromUser(
                        "Enter your query. Or 'q' to quit: "                        
                )

                if query == "quit":
                        quit = False
                        return 

                t.tic()

                result = collection.query(
                        query_texts=[query],
                        n_results=6
                )
                
                for ids, documents, metadatas, distances in zip(result["ids"], result["documents"], result["metadatas"], result["distances"]):
                        for id, document, metadata, distance in zip(ids, documents, metadatas, distances):
                                logger.info(f"ID: {id}\nDistance: {distance}\nDocument: {document}\nMetadata: {metadata}\n{'-'*40}")
                        print("\n")
                
                t.toc("Query took")