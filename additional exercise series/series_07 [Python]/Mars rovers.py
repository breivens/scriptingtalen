def turn(a: tuple, b: tuple, c: tuple):
    assert a != b and b != c and a != c, "three points must be different"
    (xa, ya), (xb, yb), (xc, yc) = a, b, c
    return min(max((xb - xa) * (yc - ya) - (yb - ya) * (xc - xa), -1), 1)


def distance(a: tuple, b: tuple):
    (xa, ya), (xb, yb) = a, b
    return ((xa - xb) ** 2 + (ya - yb) ** 2) ** .5


def next_point(a: tuple, collection: list or set or tuple, clockwise=True):
    collection = list(collection)
    b = collection[0] if collection[0] != a else collection[1]
    for c in collection:
        if c not in (a, b):
            t = turn(a, b, c)
            if t == (1 if clockwise else -1) or (t == 0 and distance(a, b) < distance(a, c)):
                b = c
    return b


def contour(collection: list or tuple, clockwise=True):
    sequence = [min(collection)]
    while (n := next_point(sequence[-1], collection, clockwise)) != sequence[0]:
        sequence.append(n)
    return sequence


punten = ((3, 3), (0, 4), (4, 4), (1, 0), (6, 2), (2, 4), (5, 5), (1, 2), (5, 2))
print(contour(punten))
print(contour(punten, False))
