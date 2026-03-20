# AIMO 3 Solver (v6)

Pipeline avanzado para la competencia Kaggle AI Mathematical Olympiad.

## Features
- Multi-attempt solving
- Attempt profiles (diversidad de razonamiento)
- Repair step
- Verifier (Sympy + Python)
- Weighted selection
- Judge / reranker (second pass)
- Cache local
- Evaluation offline
- Analysis de resultados

## Quick start

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
copy .env.example .env
```

## Run

```bash
python main.py
```

## Evaluate

```bash
python evaluate.py
```

## Analyze

```bash
python analyze_results.py
```

## Author
Facundo Olcese
