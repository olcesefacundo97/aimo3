from src.attempt_profiles import ATTEMPT_PROFILES
from src.answer_parser import parse_final_answer

class MultiAttemptSolver:
    def __init__(self, base_solver):
        self.base_solver = base_solver

    def solve(self, problem: str, num_attempts=5):
        answers = []

        for i in range(num_attempts):
            profile = ATTEMPT_PROFILES[i % len(ATTEMPT_PROFILES)]

            # simulación de perfil aplicado
            response = f"{profile['name']} -> FINAL_ANSWER: 42"

            parsed = parse_final_answer(response)
            answers.append(parsed)

        # majority vote simple
        return max(set(answers), key=answers.count)
