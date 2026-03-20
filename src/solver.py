from src.prompting import build_prompt
from src.answer_parser import parse_final_answer

class Solver:
    def solve(self, problem: str):
        # Placeholder: reemplazar con llamada real a modelo
        response = f"FINAL_ANSWER: 42"
        return parse_final_answer(response)
