import ollama


MODEL = "qwen3:0.6b"


def ask_llm(prompt: str) -> str:
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
