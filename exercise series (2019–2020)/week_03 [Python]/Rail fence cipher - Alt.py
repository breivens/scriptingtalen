def encode(line, key):
    if key == 1:
        return line
    rail = [['\n'] * len(line) for _ in range(key)]
    dir_down = False
    row, col = 0, 0

    for char in line:
        if row in (0, key - 1):
            dir_down = not dir_down

        rail[row][col] = char
        col += 1
        row += 1 if dir_down else -1

    return "".join([rail[i][j] for i in range(key) for j in range(len(line)) if rail[i][j] != '\n'])


def decode(line, key):
    if key == 1:
        return line

    rail = [['\n'] * len(line) for _ in range(key)]
    dir_down = None
    row, col = 0, 0
    for _ in line:
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1

    index = 0
    for i in range(key):
        for j in range(len(line)):
            if rail[i][j] == '*' and index < len(line):
                rail[i][j] = line[index]
                index += 1

    result = []
    row, col = 0, 0
    for _ in line:
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        row += 1 if dir_down else -1

    return "".join(result)
