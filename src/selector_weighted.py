from collections import Counter


def weighted_vote(attempts, default=0):
    scores = {}

    for a in attempts:
        ans = a.get("answer")
        if ans is None:
            continue

        score = 1.0

        if a.get("verified"):
            score += 2.0

        if a.get("verified") == ans:
            score += 1.5

        scores[ans] = scores.get(ans, 0) + score

    if not scores:
        return default

    best_score = max(scores.values())
    best = sorted([k for k, v in scores.items() if v == best_score])

    return best[0]
