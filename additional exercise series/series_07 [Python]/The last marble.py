def fill(n: int) -> list:
    from random import choices
    return choices(('white', 'black'), k=n)


def pick(urn: list or tuple) -> tuple:
    from random import sample
    return tuple(sample(range(len(urn)), k=2))


def remove(marble1: int, marble2: int, urn: list):
    if marble1 < marble2:
        marble1, marble2 = marble2, marble1
    if urn.pop(marble1) == urn.pop(marble2):
        urn.append('black')
    else:
        urn.append('white')


def last(urn: list or tuple) -> str:
    marbles = list(urn)
    for _ in range(len(marbles) - 1):
        remove(*pick(marbles), urn=marbles)
    return marbles[0]


print(last(['white', 'black', 'black', 'black', 'white', 'white', 'white', 'white', 'white']))
print(last(fill(10)))
