import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode("This is a test sentence for chunking.")
print(f"Token count: {len(tokens)}")