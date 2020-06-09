class TicTacToe:
    def __init__(self, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            self.grid = [line for line in file.read().split('\n') if line]

    def __str__(self):
        return '\n'.join([' '.join(line.replace(' ', '.')) for line in self.grid])

    def winner(self):
        def check(matrix: list):
            for row in map(set, matrix):  # horizontal
                if len(row) == 1:
                    return next(iter(row))
            for row in map(set, zip(*matrix)):  # vertical
                if len(row) == 1:
                    return next(iter(row))
            if matrix[0][0] == matrix[1][1] == matrix[2][2]:  # left diagonal
                return matrix[0][0]
            if matrix[0][2] == matrix[1][1] == matrix[2][0]:  # right diagonal
                return matrix[0][2]
            return None

        winner = check(self.grid)
        return f'{winner} wins' if winner else 'draw'


game = TicTacToe("game_01.txt")
print(game)
print(game.winner())
print()
game = TicTacToe("game_02.txt")
print(game)
print(game.winner())
print()
game = TicTacToe("game_03.txt")
print(game)
print(game.winner())
