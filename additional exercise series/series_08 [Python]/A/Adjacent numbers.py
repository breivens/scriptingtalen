def listRepresentation(sequence: str, columns: int) -> list:
    length = len(sequence)
    assert sequence.isdigit() and length % columns == 0, 'invalid string representation'
    return [list(map(int, sequence[i:i + columns])) for i in range(0, length, columns)]


def neighbours(r: int, c: int, grid: list) -> set:
    rows, columns = len(grid), len(grid[0])
    assert -1 < r < rows and -1 < c < columns, 'invalid position'
    return {grid[r + dx][c + dy]
            for dx, dy in {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}
            if -1 < r + dx < rows and -1 < c + dy < columns}


def isAdjacent(sequence: str, columns: int):
    grid = listRepresentation(sequence, columns)
    for r, row in enumerate(grid):
        for c, digit in enumerate(row):
            if digit > 1 and not set(range(1, digit)) <= neighbours(r, c, grid):
                return False
    return True
