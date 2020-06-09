from _other.help_functions import visual_plot_points_on_grid
from itertools import combinations, product


def structure(points):  # visualize n x n grid
    return visual_plot_points_on_grid(points)


def are_collinear(p1, p2, p3):
    return (p1[0] - p2[0]) * (p1[1] - p3[1]) == (p1[0] - p3[0]) * (p1[1] - p2[1])


def collinear_points(n, p1, p2):
    points = set()
    for p3 in set(product(range(n), repeat=2)):
        if are_collinear(p1, p2, p3):
            points.add(p3)
    return points


def no_three_in_line(points):
    lines = set()
    for ((x1, y1), (x2, y2)) in list(combinations(points, 2)):
        if x1 == x2:
            a = 'infinity'
            b = x1
        else:
            a = round((y2 - y1) / (x2 - x1), 3)
            b = round(y1 - a * x1, 3)
        line = (a, b)
        if line in lines:
            return False
        lines.add(line)
    return True


def non_collinear_points(n, points):
    total = {(i, j) for i in range(n) for j in range(n)}
    combos = set(combinations(points, 2))
    c_punten = set()
    for combo in combos:
        c_punten.update(collinear_points(n, combo[0], combo[1]))
    return total - c_punten
