from itertools import combinations


def are_collinear(p1, p2, p3):
    (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
    return (x1 - x2) * (y1 - y3) == (x1 - x3) * (y1 - y2)


def collinear_points(n, p1, p2):
    return {(r, c) for r in range(n) for c in range(n) if are_collinear(p1, p2, (r, c))}


def no_three_in_line(points):
    if len(points) < 3:
        return True
    for triplet in combinations(points, 3):
        if are_collinear(*triplet):
            return False
    return True


def non_collinear_points(n, points):
    free_points = {(r, c) for r in range(n) for c in range(n)}
    for pair in combinations(points, 2):
        free_points -= collinear_points(n, *pair)
    return free_points
