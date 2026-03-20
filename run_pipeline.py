from src.solver import Solver
from src.multi_solver import MultiAttemptSolver

if __name__ == "__main__":
    base = Solver()
    multi = MultiAttemptSolver(base)

    problem = "What is 8*8?"
    result = multi.solve(problem)

    print("Final answer:", result)
