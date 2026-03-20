from collections import Counter
from typing import Iterable, Optional


def majority_vote(candidates: Iterable[Optional[int]], default: int = 0) -> int:
    valid = [c for c in candidates if c is not None]
    if not valid:
        return default

    counts = Counter(valid)
    top_freq = counts.most_common(1)[0][1]
    tied = sorted([answer for answer, freq in counts.items() if freq == top_freq])
    return tied[0]
