from itertools import chain


class Inventory:
    def __init__(self, n: int, m: int):
        self.rows, self.columns = n, m
        self.grid = [['#'] * self.columns for _ in range(self.rows)]
        self.listed = {}

    def __str__(self):
        return '\n'.join(map(''.join, self.grid))

    def catalog(self, letter: str, number: int, position: str):
        assert isinstance(letter, str) and letter.isupper(), "invalid letter"
        assert letter not in self.listed, "letter already used"

        num_words = 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'ELEVEN', 'TWELVE'
        v, h = (0, 1) if position[0] == 'H' else (1, 0)  # directional offset
        r, c = [int(item) - 1 if item else -1 for item in position[1:].split(':')]  # row and column index
        tile = num_words[number - 1] + '-' + letter  # tile

        for i in range(len(tile)):  # control loop
            x, y = r + v * i, c + h * i
            assert 0 <= x < self.rows and 0 <= y < self.columns, "invalid position"
            assert self.grid[x][y] == '#', "position already used"

        for char in tile:  # assign loop
            self.grid[r][c] = char
            r += v
            c += h

        self.listed[letter] = number
        return self

    def listed_occurrences(self):
        return self.listed

    def observed_occurrences(self):
        grid = tuple(chain(*self.grid))
        return {char: grid.count(char) for char in set(grid) if char.isalpha()}

    def complete(self):
        return '#' not in set(chain(*self.grid))

    def self_descriptive(self):
        return self.complete() and self.listed_occurrences() == self.observed_occurrences()
