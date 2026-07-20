from transformers import pipeline
import torch

def generateArtifactContext(generator, prev_section: str, current_content: str, next_section: str) -> str:
        """
        Takes the surrounding text chunks and the current artifact,
        and uses the LLM to generate a clean 2-3 sentence summary.
        """
        prompt = (
                f"<|im_start|>system\n"
                f"You are a precise academic summarizer. Your only job is to write a single, clean 2-3 sentence summary of the current chunk. "
                f"Use the previous and next chunks only to inform your understanding — do not summarize them. "
                f"Rules: no markdown, no bullet points, no headers, no newlines, no internal thoughts, no meta-commentary, no repetition of these instructions. "
                f"Output only the summary paragraph and nothing else.<|im_end|>\n"
                f"<|im_start|>user\n"
                f"Previous chunk:\n{prev_section}\n\n"
                f"Current chunk:\n{current_content}\n\n"
                f"Next chunk:\n{next_section}\n"
                f"<|im_end|>\n"
                f"<|im_start|>assistant\n"
        )

        generation = generator(prompt, max_new_tokens=150, return_full_text=False)
        return generation[0]["generated_text"].strip()

def initializeTransformer() -> pipeline:
        generator = pipeline("text-generation", model="Qwen/Qwen2.5-3B-Instruct", device = 0 if torch.cuda.is_available() else -1)
        return generator