import os
from openai import OpenAI

from src.prompting import build_prompt
from src.answer_parser import parse_final_answer


class LLMSolver:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("Missing OPENAI_API_KEY in environment")

        self.client = OpenAI(api_key=api_key)
        self.model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    def solve(self, problem: str) -> int:
        prompt = build_prompt(problem)

        response = self.client.responses.create(
            model=self.model,
            temperature=0.2,
            input=prompt,
        )

        text = response.output_text
        return parse_final_answer(text)
