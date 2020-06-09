def list_representation(sequence: list or tuple, rows, columns=None):
    return [list(map(int, row)) for row in zip(*[iter(sequence)] * (columns or rows))]


def string_representation(matrix: list):
    return ''.join([''.join(map(str, row)) for row in matrix]), len(matrix), len(matrix[0])


def move(number: int, positions: set, grid: list):
    for r, row in enumerate(grid):
        for c in range(len(row)):
            if (r, c) in positions:
                grid[r][c] += number
    return grid


def is_solved(grid: list):
    return len(set.union(*(map(set, grid)))) == 1


def adjacent(position: tuple, grid: list, added: list):
    r, c = position
    return {(r + x, c + y) for (x, y) in ((-1, 0), (0, 1), (1, 0), (0, -1))
            if -1 < r + x < len(grid)
            and -1 < c + y < len(grid[0])
            and (r + x, c + y) not in added
            and grid[r][c] == grid[r + x][c + y]}


def group(position: tuple, grid: list):
    grouped = [position]
    while True:
        subgrouped = list()
        for pos in grouped:
            subgrouped.extend(adjacent(pos, grid, grouped))
        if not subgrouped:
            break
        grouped.extend(subgrouped)
    return set(grouped)


def is_solution(positions: list, grid: list):
    from copy import deepcopy
    new_grid = deepcopy(grid)
    for (r, c, b) in positions:
        new_grid = move(1 if b else -1, group((r, c), new_grid), new_grid)
    return is_solved(new_grid)
