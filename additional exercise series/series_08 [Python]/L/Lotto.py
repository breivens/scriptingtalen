def lottery(count=6, maximum=42) -> str:
    from random import sample
    balls = sample(range(1, maximum + 1), count)
    return ' - '.join(map(str, sorted(balls)))


print(lottery())
