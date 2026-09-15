from llm import ask_llm


def create_research_plan(question: str) -> str:

    prompt = f"""
You are the research planning brain of Jarvis.

The user has asked:

{question}

Do NOT answer the question.

Instead, create a research plan.

Identify:
1. The main objective
2. Important topics to investigate
3. Different aspects that require separate research
4. What types of sources should be consulted
5. What information needs verification

Return a clear and structured research plan.
"""

    return ask_llm(prompt)
