class WordSquare:
    def __init__(self, order: int, string: str):
        assert order * (order + 1) // 2 == len(string), 'invalid square'
        self.order = order
        self.square = [[''] * self.order for _ in range(self.order)]
        string = string.upper()
        for r in range(self.order):
            for c, char in enumerate(string[:r + 1]):
                self.square[r][c] = self.square[c][r] = char
            string = string[r + 1:]

    def __repr__(self):
        return '\n'.join(map(''.join, self.square))

    def letter(self, r: int, c: int) -> str:
        assert -1 < r < self.order and -1 < c < self.order, "invalid index"
        return self.square[r][c]

    def word(self, r: int) -> str:
        assert -1 < r < self.order, "invalid index"
        return ''.join(self.square[r])

    def valid(self, path: str) -> bool:
        with open(path, "r", encoding='utf-8') as f:
            words = set(f.read().upper().split('\n'))
        return set(map(''.join, self.square)) <= words
