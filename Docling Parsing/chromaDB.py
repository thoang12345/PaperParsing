import chromadb
import re
import functions as fun
from dataclasses import dataclass

def split_chunks(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Split on "=== Chunk X===" while keeping the chunk number
    pattern = r"=== Chunk (\d+)==="
    parts = re.split(pattern, text)

    chunks = {}

    # parts will look like: [before, id1, content1, id2, content2, ...]
    for i in range(1, len(parts), 2):
        chunk_id = int(parts[i])
        content = parts[i + 1].strip()
        chunks[chunk_id] = content

    return chunks

# Set the options for the pipeline
@dataclass
class PipelineConfig:
    addElements: bool = True
    ImageScale: float = 2.7
    doOcr: bool = True
    tableStructure: bool = True
    ocrBatchSize: int = 32
    layoutBatchSize: int = 32
    tableBatchSize: int = 4
    
config = PipelineConfig()
converter, generator, tokenizer = fun.initializeStuff(config)
client = chromadb.PersistentClient(r"F:\Research Program thing\McNair\Navy stuff\DocLing Parsing\chromaDB")
collection = client.get_or_create_collection(name="my_papers")
pathToFile = r"F:\Research Program thing\McNair\Navy stuff\DocLing Parsing\Output Motor Skid\2408.09869v5\2408.09869v5_chunks.md"
chunks = split_chunks(pathToFile)
sorted_items = sorted(chunks.items())

collection.add(
    documents=[content for _, content in sorted_items],
    ids=[f"chunk_{i:03d}" for i, _ in sorted_items]
)


results = collection.query(
    query_texts=["What is Docling?"],
    n_results=5
)

context = "\n\n".join(results["documents"][0])

prompt = f"""
Answer the question using the context below:

{context}

Question: What is Docling?
"""
print(prompt)

answer = generator(prompt, truncation=True, return_full_text=False, batch_size=1)[0]

print("\nAnswer:\n", answer)