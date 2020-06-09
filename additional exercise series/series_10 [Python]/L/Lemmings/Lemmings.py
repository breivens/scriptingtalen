class Lemming:
    def __init__(self, path: str, column: int, direction: str):
        with open(path, 'r', encoding='utf-8') as file:
            self.level = [list(row) for row in file.read().split('\n') if row]

        for row in range(len(self.level) - 1):
            if self.level[row][column] == ' ' and self.level[row + 1][column] == '#':
                self.current = row, column, direction
                break

    def __str__(self):
        cr, cc, d = self.current
        return '\n'.join(
            [''.join([d if (r, c) == (cr, cc) else column for c, column in enumerate(row)])
             for r, row in enumerate(self.level)])

    def position(self):
        return self.current

    def step(self):
        r, c, d = self.current
        offset = 1 if d == '>' else -1
        if self.level[r][c + offset] == ' ':  # horizontal
            self.current = r, c + offset, d
        elif self.level[r - 1][c + offset] == ' ':  # horizontal + up
            self.current = r - 1, c + offset, d
        else:  # turn
            self.current = r, c, '<' if d == '>' else '>'

        i, (r, c, d) = 1, self.current
        while self.level[r + i][c] != '#':  # while no footing
            i += 1
        self.current = r + i - 1, c, d
        return self.current

    def steps(self, n: int):
        return [self.step() for _ in range(n)]


lemming = Lemming('level_11.txt', 2, '<')
print(lemming)
