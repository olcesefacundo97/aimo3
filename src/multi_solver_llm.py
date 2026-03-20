from src.attempt_profiles import ATTEMPT_PROFILES
from src.selector import majority_vote


class MultiAttemptLLMSolver:
    def __init__(self, llm_solver):
        self.llm_solver = llm_solver

    def solve(self, problem: str, num_attempts=5):
        answers = []

        for i in range(num_attempts):
            profile = ATTEMPT_PROFILES[i % len(ATTEMPT_PROFILES)]

            # prepend instruction to diversify reasoning
            modified_problem = f"{profile['instruction']}\n\n{problem}"

            try:
                answer = self.llm_solver.solve(modified_problem)
                answers.append(answer)
            except Exception:
                continue

        return majority_vote(answers, default=0)
