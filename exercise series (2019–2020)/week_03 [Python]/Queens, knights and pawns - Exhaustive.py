def schaakbord(rows, columns, pieces):
    board = [[""] * columns for _ in range(rows)]
    for piece, r, c in pieces:
        board[r][c] = piece
    return board


def horse(rows, columns, board):
    reachable = ((rows + 1, columns + 2), (rows + 1, columns - 2), (rows - 1, columns + 2), (rows - 1, columns - 2),
                 (rows + 2, columns + 1), (rows + 2, columns - 1), (rows - 2, columns + 1), (rows - 2, columns - 1))
    for i in range(8):
        try:
            if reachable[i][0] >= 0 and reachable[i][1] >= 0 and board[reachable[i][0]][reachable[i][1]] == "":
                board[reachable[i][0]][reachable[i][1]] = "*"
        except IndexError:
            pass
    return board


def orthogonal(rows, columns, board):
    max_length = len(board) if len(board) > len(board[0]) else len(board[0])
    # horizontal - right
    for i in range(columns + 1, max_length):
        try:
            if board[rows][i] == "":
                board[rows][i] = "*"
            elif board[rows][i] in "KQP":
                break
        except IndexError:
            pass

    # horizontal - left
    for i in range(columns - 1, -1, -1):
        try:
            if board[rows][i] == "":
                board[rows][i] = "*"
            elif board[rows][i] in "KQP":
                break
        except IndexError:
            pass

    # vertical - down
    for i in range(rows + 1, max_length):
        try:
            if board[i][columns] == "":
                board[i][columns] = "*"
            elif board[i][columns] in "KQP":
                break
        except IndexError:
            pass

    # vertical - up
    for i in range(rows - 1, -max_length, -1):
        try:
            if i < 0:
                break
            elif board[i][columns] == "":
                board[i][columns] = "*"
            elif board[i][columns] in "KQP":
                break
        except IndexError:
            pass

    return board


def diagonal(rows, columns, board):
    max_length = len(board) if len(board) > len(board[0]) else len(board[0])
    # diagonal \ - right-down
    for i in range(1, max_length):
        try:
            if board[rows + i][columns + i] == "":
                board[rows + i][columns + i] = "*"
            elif board[rows + i][columns + i] in "KQP":
                break
        except IndexError:
            pass

    # diagonal \ - left-up
    for i in range(1, max_length):
        try:
            if rows - i < 0 or columns - i < 0:
                break
            elif board[rows - i][columns - i] == "":
                board[rows - i][columns - i] = "*"
            elif board[rows - i][columns - i] in "KQP":
                break
        except IndexError:
            pass

    # check diagonal / - left-down
    for i in range(1, max_length):
        try:
            if rows + i < 0 or columns - i < 0:
                break
            elif board[rows + i][columns - i] == "":
                board[rows + i][columns - i] = "*"
            elif board[rows + i][columns - i] in "KQP":
                break
        except IndexError:
            pass

    # check diagonal / - right-up
    for i in range(1, max_length):
        try:
            if rows - i < 0 or columns + i < 0:
                break
            if board[rows - i][columns + i] == "":
                board[rows - i][columns + i] = "*"
            elif board[rows - i][columns + i] in "KQP":
                break
        except IndexError:
            pass

    return board


def queen(rows, columns, board):
    board = orthogonal(rows, columns, board)
    board = diagonal(rows, columns, board)
    return board


def onveilige_vierkanten(rows, columns, pieces):
    board = schaakbord(rows, columns, pieces)
    for i, irows in enumerate(board):
        for j, jcolumn in enumerate(irows):
            if jcolumn == "K":
                board = horse(i, j, board)
            elif jcolumn == "Q":
                board = queen(i, j, board)
    return board


def veilige_vierkanten(rows, columns, pieces):
    return sum(onveilige_vierkanten(rows, columns, pieces), []).count('')
