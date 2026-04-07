import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode("This is a test sentence for chunking.")
print(f"Token count: {len(tokens)}")

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "Qwen/Qwen2.5-3B-Instruct"

print("Downloading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("Downloading model weights (~6GB, this will take a while)...")
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,  # saves disk space vs float32
    device_map="auto"
)

print("Done! Model is cached locally.")