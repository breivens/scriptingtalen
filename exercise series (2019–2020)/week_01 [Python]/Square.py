from itertools import combinations


def distance(p1, p2):
    return round(((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** (1 / 2), 10)


floats = tuple((float(input()), float(input())) for _ in range(4))
distances = {distance(p1, p2) for p1, p2 in combinations(floats, 2)}
print("square" if len(distances) == 2 else "not a square")

"""
# ---------------------------------------------------------------------------------------------------- #


def distance(p1, p2):
    return round(((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** (1 / 2), 10)


a = float(input()), float(input())
b = float(input()), float(input())
c = float(input()), float(input())
d = float(input()), float(input())
distances = {distance(a, b), distance(b, c), distance(c, d), distance(d, a), distance(a, c), distance(b, d)}
print("square" if len(distances) == 2 else "not a square")


# ---------------------------------------------------------------------------------------------------- #


def distance(p1, p2):
    return round(((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** (1 / 2), 10)


points = []
distances = []
for other in range(4):
    point = (float(input()), float(input()))
    distances.extend([distance(point, &) for & in points])
    points.append(point)
print("square" if len(set(distances)) <= 2 else "not a square")


# ---------------------------------------------------------------------------------------------------- #


def distance(p1, p2):
    return round(((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** (1 / 2), 10)


points = [(float(input()), float(input())) for other in range(4)]
distances = {distance(points[0], points[1]), distance(points[1], points[2]), distance(points[2], points[3]),
             distance(points[3], points[0]), distance(points[0], points[2]), distance(points[1], points[3])}
print("square" if len(distances) == 2 else "not a square")
"""
