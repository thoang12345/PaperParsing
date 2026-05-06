import chromadb
import functions as fun

fun.clear_terminal()

# Connect to the existing database
client = chromadb.PersistentClient(path=r"C:\Users\mayhe\OneDrive\Documents\GitHub\PaperParsing\Docling Parsing\chromadb")
collection = client.get_collection(name="The_Mass")

print(f"Connected to '{collection.name}' — {collection.count()} chunks in database")

while True:
    query = input("\nEnter query or 'quit' to exit. \n")

    if query == "quit":
        print("\nBye Bye!")
        break
    
    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    for i, doc in enumerate(results["documents"][0]):
        meta = results["metadatas"][0][i]
        print(f"\n--- Result {i+1} ---")
        print(f"Doc: {meta.get('docName')} | Page: {meta.get('pageStart')} | Chunk: {meta.get('chunkNum')}")
        print(f"Headers: {meta.get('headers')}")
        print(f"Context: {meta.get('context')}")
        print(f"\n{doc}")