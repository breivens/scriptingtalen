def kangaroo(k: str, j: str) -> bool:
    from re import match
    pattern = '?'.join(k.lower()) + '?'
    return bool(match('^' + pattern + '$', j.lower()))


def joeys(k: str, sequence: list or tuple or set) -> set:
    return {j for j in sequence if kangaroo(k, j)}
