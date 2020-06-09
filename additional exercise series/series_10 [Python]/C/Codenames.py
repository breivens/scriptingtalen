class GameBoard:
    def __init__(self, rows: int, columns: int, key: str):
        self.game_over = False
        self.board = [['?'] * columns for _ in range(rows)]
        self.key = key
        self.rows, self.columns = rows, columns
        self.red = self.blue = 0
        self.RED, self.BLUE = key.count('R'), key.count('B')
        self.current_color = 'R' if self.RED > self.BLUE else 'B'

    def __str__(self):
        return '\n'.join(map(' '.join, self.board))

    def isover(self):
        return self.game_over

    def turn(self):
        assert not self.game_over, "game over"
        return self.current_color

    def select(self, r: int, c: int):
        assert not self.game_over, "game over"
        if self.board[r][c] == '?':
            selected = self.key[r * self.columns + c]
            if selected != self.current_color:
                self.stop().game_over = selected == 'X'
            if selected == 'R':
                self.red += 1
                self.game_over = self.red == self.RED
            elif selected == 'B':
                self.blue += 1
                self.game_over = self.blue == self.BLUE
            self.board[r][c] = selected
        return self

    def stop(self):
        assert not self.game_over, "game over"
        self.current_color = 'R' if self.current_color == 'B' else 'B'
        return self


board_03 = GameBoard(5, 4, '--RBB-XBRB-BRRBRRRRB')
print(board_03.turn())
print(board_03.select(1, 2))
print(board_03.turn())
print(board_03.isover())
