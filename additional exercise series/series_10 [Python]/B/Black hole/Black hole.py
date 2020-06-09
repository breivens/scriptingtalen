class BlackHole:
    def __init__(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            from itertools import chain
            content = f.read()
            self.board = [x.split() for x in content.split('\n') if x]
            stones = tuple(chain(*self.board))
        check = {'*', 'X'}
        for i in range(1, 16):
            check |= {f'{i}R', f'{i}B'}
        assert (set(stones) == check
                and (stones.count('*'), stones.count('X'), content.count(' ')) == (5, 1, 28)
                and tuple(map(len, self.board)) == (1, 2, 3, 4, 5, 6, 7, 8)), 'invalid board'

    def score(self):
        score_r = score_b = 75
        rx = cx = 0
        for r, row in enumerate(self.board):
            if 'X' in row:
                rx, cx = r, row.index('X')
                break
        for r, c in {(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)}:
            rn, cn = rx + r, cx + c
            if -1 < rn < 8 and -1 < cn < rn + 1:
                if (stone := self.board[rn][cn]) != '*':
                    color, value = stone[-1], int(stone[:-1])
                    score_r += value if color == 'R' else -value
                    score_b += value if color == 'B' else -value
        return score_r, score_b


b = BlackHole('valid_board.txt')
print(b.score())