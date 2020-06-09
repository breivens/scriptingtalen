def rail_fence(rows, columns):
    period = tuple(range(rows)) + tuple(range(rows - 2, 0, -1))
    return [period[i % len(period)] for i in range(columns)]


def encode(text, rows):
    fence = rail_fence(rows, len(text))
    return "".join(char for row in range(rows) for column, char in enumerate(text) if fence[column] == row)


def decode(text, rows):
    fence = rail_fence(rows, len(text))
    index = 0
    for row in range(rows):
        for column in range(len(text)):
            if fence[column] == row:
                fence[column] = text[index]
                index += 1
    return "".join(fence)
