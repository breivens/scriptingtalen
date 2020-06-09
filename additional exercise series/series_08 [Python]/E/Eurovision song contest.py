def addScores(scoreboard: dict, scores: dict):
    for country, score in scores.items():
        if country not in scoreboard:
            scoreboard[country] = 0
        scoreboard[country] += score


def showScores(scoreboard: dict, n=None) -> list:
    from functools import cmp_to_key

    def cmp(x, y):
        (cx, sx), (cy, sy) = x, y
        if sx < sy or (sx == sy and cx > cy):
            return 1
        return -1

    n = n or len(scoreboard)
    return sorted(scoreboard.items(), key=cmp_to_key(cmp))[:n]
