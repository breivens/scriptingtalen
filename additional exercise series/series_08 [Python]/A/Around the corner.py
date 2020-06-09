def ispolygon(sequence: list or tuple):
    return (isinstance(sequence, (list, tuple))
            and len(sequence) >= 3
            and all(isinstance(item, str) and item.isalpha() and item.isupper() for item in sequence)
            and len(set(map(len, sequence))) == 1)


def solution(polygon: list or tuple, start=0, clockwise=True):
    assert ispolygon(polygon), "invalid polygon"
    length = len(polygon)
    clockwise = 1 if clockwise else -1
    return "".join([polygon[(start + i * clockwise) % length][i] for i in range(len(polygon[0]))])


def solutions(polygon, clockwise=None):
    assert ispolygon(polygon), "invalid polygon"
    solutions = set()
    for i in range(len(polygon)):
        if clockwise in {True, None}:
            solutions.add(solution(polygon, start=i, clockwise=True))
        if clockwise in {False, None}:
            solutions.add(solution(polygon, start=i, clockwise=False))
    return solutions
