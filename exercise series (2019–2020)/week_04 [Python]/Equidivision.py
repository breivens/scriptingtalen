from other.help_functions import visual_grid, visual_plot_points_on_grid
from itertools import chain, combinations


def full_grid_repr(grid):  # visualize filled n x n grid
    return visual_grid(grid)


def group_repr(points, *length):  # visualize points on a grid
    return visual_plot_points_on_grid(points, *length)


def groups(grid):  # because it's an n x n grid, every nth element is a new row
    output = {}
    for i, label in enumerate(chain(*grid)):
        r = i // len(grid)
        k = i % len(grid)
        if label in output:
            output[label].add((r, k))
        else:
            output[label] = {(r, k)}
    return output


def connected(group):  # for n cells there must be at least n-1 connections
    return sum(1 for (x1, y1), (x2, y2) in set(combinations(group, 2)) if
               x1 == x2 and y1 - y2 in (1, -1) or (y1 == y2 and x1 - x2 in (1, -1))) >= len(group) - 1


def equidivision(grid):
    length = len(next(iter(grouped := groups(grid).values())))  # first group as check
    for group in grouped:
        if length != len(group) or not connected(group):  # check if every group has the same length and is connected
            return False
    return True


points = [[1, 1, 1, 5, 5], [2, 1, 5, 5, 4], [2, 1, 5, 4, 4], [2, 2, 4, 4, 3], [2, 3, 3, 3, 3]]
print(full_grid_repr(points), end="\n\n")

gruppen = groups(points)
for gruppe in gruppen:
    print(group_repr(gruppen[gruppe], len(gruppen)), end="\n\n")
