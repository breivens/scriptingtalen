def knight(r: int, c: int) -> list:
    return [(r + x, c + y)
            for x, y in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
            if -1 < r + x < 8 and -1 < c + y < 8]


def rook(r: int, c: int) -> list:
    positions = []
    for x, y in ((-1, 0), (0, -1), (0, 1), (1, 0)):
        dx, dy = r + x, c + y
        while -1 < dx < 8 and -1 < dy < 8:
            positions.append((dx, dy))
            dx += x
            dy += y
    return sorted(positions)


def queen(r: int, c: int) -> list:
    positions = []
    for x, y in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        dx, dy = r + x, c + y
        while -1 < dx < 8 and -1 < dy < 8:
            positions.append((dx, dy))
            dx += x
            dy += y
    return sorted(positions)


def tour(chessboard: list, piece=knight, closed=False) -> bool:
    def find(square: int, chessboard: list) -> tuple:
        for r, row in enumerate(chessboard):
            if square in row:
                return r, row.index(square)
        raise AssertionError('invalid square')

    def reachable(piece, square: int, row: int, column: int) -> tuple:
        for r, c in piece(row, column):
            if square == chessboard[r][c]:
                return r, c
        raise AssertionError('unreachable')

    r, c = find(1, chessboard)  # find starting row and column

    for i in range(2, 65):  # iterate over 2 -> 64
        try:
            r, c = reachable(piece=piece, square=i, row=r, column=c)
        except AssertionError:
            return False
    return True if not closed else (1 in {chessboard[r][c] for r, c in piece(r, c)})


chessboard = [[3, 22, 49, 56, 5, 20, 47, 58],
              [50, 55, 4, 21, 48, 57, 6, 19],
              [23, 2, 53, 44, 25, 8, 59, 46],
              [54, 51, 24, 1, 60, 45, 18, 7],
              [15, 36, 43, 52, 17, 26, 9, 62],
              [42, 39, 16, 33, 12, 61, 30, 27],
              [35, 14, 37, 40, 29, 32, 63, 10],
              [38, 41, 34, 13, 64, 11, 28, 31]]

print(tour(chessboard, knight))
print(tour(chessboard, rook))
print(tour(chessboard, queen))
