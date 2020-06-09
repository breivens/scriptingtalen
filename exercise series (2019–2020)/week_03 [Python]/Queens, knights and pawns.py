from itertools import chain


def structure(board):  # visualize n x n grid
    return "\n".join([" ".join(["-" if columns == "" else columns for columns in rows]) for rows in board])


def chessboard(rows, columns, pieces):
    board = [[""] * columns for _ in range(rows)]
    for piece, r, c in pieces:
        board[r][c] = piece
    return board


def _knight(knight, rows, columns, board):
    for x, y in ((-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2)):
        x, y = knight[1] + x, knight[2] + y
        if 0 <= x < rows and 0 <= y < columns and board[x][y] == "":
            board[x][y] = "*"


def _queen(queen, rows, columns, board):
    for direction in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        x, y = queen[1], queen[2]
        while 0 <= x < rows and 0 <= y < columns and board[x][y] not in ("K", "P"):
            if board[x][y] == "":
                board[x][y] = "*"
            x += direction[0]
            y += direction[1]


def unsafe_squares(rows, columns, pieces):
    board = chessboard(rows, columns, pieces)
    for piece in pieces:
        if piece[0] == 'K':
            _knight(piece, rows, columns, board)
        elif piece[0] == 'Q':
            _queen(piece, rows, columns, board)
    return board


def veilige_vierkanten(rows, columns, pieces):
    return list(chain(*unsafe_squares(rows, columns, pieces))).count("")
