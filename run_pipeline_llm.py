from src.llm_solver import LLMSolver
from src.multi_solver_llm import MultiAttemptLLMSolver

if __name__ == "__main__":
    solver = LLMSolver()
    multi_solver = MultiAttemptLLMSolver(solver)

    problem = "What is 12*12?"
    result = multi_solver.solve(problem)

    print("Final answer:", result)
