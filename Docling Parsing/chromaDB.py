import chromadb
import functions as fun
from pytictoc import TicToc

fun.clear_terminal()

# Connect to the existing database
client = chromadb.PersistentClient(path=r"C:\Users\THIENAN\Documents\GitHub\PaperParsing\Docling Parsing\chromadb")
collection = client.get_collection(name="The_Mass")
t = TicToc()

print(f"Connected to '{collection.name}' — {collection.count()} chunks in database")

fun.queryDatabase(t, collection)

    