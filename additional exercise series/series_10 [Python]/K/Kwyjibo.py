class Scrabble:

    def __init__(self, n: int):
        assert 1 <= n <= 26, "invalid gameboard"
        from string import ascii_uppercase
        self.alphabet = ascii_uppercase
        self.dimension = n
        self.board = [['-'] * n for _ in range(n)]

    def __str__(self):
        return "\n".join(map("".join, self.board))

    def place(self, position: str, word: str):
        from itertools import groupby

        string, (r, c) = "", ["".join(g[1]) for g in groupby(position, key=str.isdigit)]

        r, c, v, h = (int(r) - 1, self.alphabet.index(c), 0, 1) if r.isdigit() else (
            int(c) - 1, self.alphabet.index(r), 1, 0)

        for i, char in enumerate(word):  # control loop
            nr, nc = r + v * i, c + h * i
            assert (0 <= nr < self.dimension and 0 <= nc < self.dimension  # out of bounds
                    and self.board[nr][nc].lower() in ('-', word[i].lower())), "word cannot be placed"

        group = ""
        for char in word:  # assign loop
            if self.board[r][c].lower() == char.lower():
                group += f"{self.board[r][c]}"
            else:
                if group:
                    string += f"({group})"
                    group = ""
                string += char
                self.board[r][c] = char
            r += v
            c += h
        return string + (f"({group})" if group else "")


board = Scrabble(42)

