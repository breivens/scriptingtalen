def lettervalue(values: list or tuple) -> dict:
    keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return dict(zip(keys, values))


def wordvalue(word: str, values: dict):
    l2v = lettervalue(values)
    return sum(l2v.get(char, 0) for char in word.upper())
