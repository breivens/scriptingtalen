class WordSearch:
    directions = {'LR': (0, 1), 'RL': (0, -1), 'TD': (1, 0), 'BU': (-1, 0)}

    def __init__(self, rows: int, columns: int, string: str):
        length = len(string)
        assert length == rows * columns, "too few letters given"
        self._rows = rows
        self._columns = columns
        self.grid = [string[i:i + columns].upper() for i in range(0, length, columns)]

    def __str__(self):
        return '\n'.join(map(''.join, self.grid))

    def rows(self):
        return self._rows

    def columns(self):
        return self._columns

    def read(self, r: int, c: int, d: str, length: int):
        string = ""
        dx, dy = WordSearch.directions[d]

        for _ in range(length):
            if not (-1 < r < self._rows and -1 < c < self._columns):
                return ''

            string += self.grid[r][c]
            r, c = r + dx, c + dy

        return string

    def search(self, word: str):
        word = word.upper()
        for r, row in enumerate(self.grid):  # horizontal
            row = row.upper()
            if word in row:  # left -> right
                return r, row.index(word), 'LR'

            row = row[::-1]
            if word in row:  # right -> left
                return r, self._columns - 1 - row.index(word), 'RL'

        for c, column in enumerate(map(''.join, zip(*self.grid))):  # vertical
            column = column.upper()
            if word in column:  # top -> bottom
                return column.index(word), c, 'TD'

            column = column[::-1]
            if word in column:  # bottom -> top
                return self._rows - 1 - column.index(word), c, 'BU'

        return None

    def solution(self, sequence: list):
        grid = list(map(list, self.grid))

        for word in sequence:
            searched = self.search(word)
            if searched:
                r, c, d = searched
                dx, dy = WordSearch.directions[d]

                for letter in word:
                    grid[r][c], r, c = letter.lower(), r + dx, c + dy

        return ''.join([letter for row in grid for letter in row if letter.isupper()])
