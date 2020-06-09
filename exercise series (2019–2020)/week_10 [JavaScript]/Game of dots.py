from itertools import chain, zip_longest


class Pipopipette:
    def __init__(self, m: int, n=None):
        self.m, self.n = m, n or m
        self._score = {'A': 0, 'B': 0}
        self._player = 'A'

        self.dots = [['+'] * self.n for _ in range(self.m)]
        self.squares = [['?'] * (self.n - 1) for _ in range(self.m - 1)]
        self.hl = [['.'] * (self.n - 1) for _ in range(self.m)]
        self.vl = [['.'] * self.n for _ in range(self.m - 1)]

    def __str__(self):
        return '\n'.join(map(''.join, self.merge([self.merge(self.dots[i], self.hl[i]) for i in range(self.m)],
                                                 [self.merge(self.vl[i], self.squares[i]) for i in range(self.m - 1)])))

    @staticmethod
    def merge(a: list or tuple, b: list or tuple):
        return list(chain(*[(x, y) if y else [x] for x, y in zip_longest(a, b)]))

    def score(self):
        return tuple(self._score.values())

    def player(self):
        return self._player

    def swap_players(self):
        self._player = 'A' if self._player == 'B' else 'B'

    def claim(self, position: str):
        from re import match
        assert match("^[HV][0-9]+,[0-9]+$", position), "invalid position"
        player, scored = self.player(), False
        direction, (r, c) = position[0], map(int, position[1:].split(','))
        assert -1 < r < self.m and -1 < c < self.n, "invalid position"

        if direction == 'H':
            assert self.hl[r][c] == '.', "dots already connected"
            self.hl[r][c] = '-'
            scored = self.check(r, c, player, horizontal=True)
        elif direction == 'V':
            assert self.vl[r][c] == '.', "dots already connected"
            self.vl[r][c] = '|'
            scored = self.check(r, c, player, horizontal=False)

        if not scored:
            self.swap_players()
        return self

    def check(self, r: int, c: int, player: str, horizontal=True):
        squares_formed = 0
        for i in (-1, 1):
            if horizontal and -1 < r + i < self.m:  # check if square is formed above or below
                if (self.hl[r + i][c] == '-'
                        and self.vl[r - (i == -1)][c] == '|'
                        and self.vl[r - (i == -1)][c + 1] == '|'
                        and self.squares[r - (i == -1)][c] == "?"):
                    self.squares[r - (i == -1)][c] = player
                    squares_formed += 1
            elif not horizontal and -1 < c + i < self.n:  # check if square is formed left or right
                if (self.vl[r][c + i] == '|'
                        and self.hl[r][c - (i == -1)] == '-'
                        and self.hl[r + 1][c - (i == -1)] == '-'
                        and self.squares[r][c - (i == -1)] == "?"):
                    self.squares[r][c - (i == -1)] = player
                    squares_formed += 1

        self._score['A'] += squares_formed * (player == 'A')
        self._score['B'] += squares_formed * (player == 'B')
        return squares_formed > 0


game = Pipopipette(3)
