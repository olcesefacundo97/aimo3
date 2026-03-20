import math
import re
from typing import Optional

import sympy as sp


def extract_python_block(text: str) -> Optional[str]:
    if not text:
        return None
    match = re.search(r"```python\s*(.*?)```", text, flags=re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else None


def extract_candidate_expression(text: str) -> Optional[str]:
    if not text:
        return None

    patterns = [
        r"FINAL_EXPR:\s*([^\n]+)",
        r"\\boxed\{([^}]+)\}",
        r"\b(?:x|n|ans|answer)\s*=\s*([^\n,;]+)",
        r"\bthe answer is\s+([^\n,;]+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            expr = match.group(1).strip()
            if expr:
                return expr

    return None


def verify_with_sympy(raw_output: str) -> Optional[int]:
    expr = extract_candidate_expression(raw_output)
    if not expr:
        return None

    try:
        expr = expr.replace('^', '**').replace('−', '-')
        value = sp.sympify(expr, locals={'pi': sp.pi, 'E': sp.E})
        simplified = sp.simplify(value)
        if simplified.is_integer is True:
            answer = int(simplified)
            return answer if answer >= 0 else None
    except Exception:
        return None

    return None


def verify_with_python_block(raw_output: str) -> Optional[int]:
    code = extract_python_block(raw_output)
    if not code:
        return None

    banned = [
        'import os', 'import sys', 'open(', '__import__', 'exec(', 'eval(',
        'subprocess', 'socket', 'pathlib', 'shutil', 'requests'
    ]
    lowered = code.lower()
    if any(token in lowered for token in banned):
        return None

    safe_globals = {
        '__builtins__': {
            'abs': abs,
            'min': min,
            'max': max,
            'sum': sum,
            'range': range,
            'len': len,
            'print': print,
        },
        'math': math,
    }
    safe_locals = {}

    try:
        exec(code, safe_globals, safe_locals)
    except Exception:
        return None

    for key in ('answer', 'final_answer', 'result'):
        value = safe_locals.get(key)
        try:
            if value is not None:
                value = int(value)
                if value >= 0:
                    return value
        except Exception:
            pass

    return None


def verify_attempt(raw_output: str) -> Optional[int]:
    sympy_answer = verify_with_sympy(raw_output)
    if sympy_answer is not None:
        return sympy_answer
    return verify_with_python_block(raw_output)
