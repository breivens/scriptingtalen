def numbers(grid: list):
    return {column for row in grid for column in row}


def sums(grid: list):
    sums, n, transposed_grid = set(), len(grid), tuple(zip(*grid))
    diagonal = antidiagonal = 0
    for i in range(n):
        sums.update({sum(grid[i]), sum(transposed_grid[i])})
        diagonal += grid[i][i]
        antidiagonal += grid[i][n - i - 1]
    return sums | {diagonal, antidiagonal}


def isdistinct(grid: list):
    return len(numbers(grid)) == len(grid) ** 2


def ismagic(grid: list):
    return isdistinct(grid) and len(sums(grid)) == 1


def ishetero(grid: list):
    return isdistinct(grid) and len(sums(grid)) != 1


def isantimagic(grid: list):
    numbers = sums(grid)
    return ishetero(grid) and sorted(numbers) == list(range(min(numbers), max(numbers) + 1))
