import re

def parse_final_answer(text: str):
    match = re.search(r"FINAL_ANSWER:\s*([0-9]+)", text)
    if match:
        return int(match.group(1))
    nums = re.findall(r"\b([0-9]+)\b", text)
    return int(nums[-1]) if nums else 0
