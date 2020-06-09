class Die:
    def __init__(self):
        self.die = [[' ', '3', ' ', ' '], ['2', '6', '5', '1'], [' ', '4', ' ', ' '], [' ', ' ', ' ', ' ']]

    def __str__(self):
        return '\n'.join([' '.join(row).rstrip() for row in self.die[:-1]])

    def topNumber(self):
        return int(self.die[1][1])

    def turn(self, direction: str):
        assert direction in ('E', 'N', 'S', 'W'), "invalid direction"
        from collections import deque

        if direction in 'NS':
            self.roll()
        die = deque(self.die[1])
        die.rotate(1 if direction in 'ES' else -1 if direction in 'NW' else 0)
        self.die[1] = list(die)
        if direction in 'NS':
            self.roll()
        return self.topNumber()

    def roll(self):
        self.die = list(map(list, zip(*self.die)))  # transposition
        self.die[1][-1], self.die[-1][1] = self.die[-1][1], self.die[1][-1]  # reposition bottom

    def sequence(self, target: int):
        sequence, top = list(), self.topNumber()
        while not (top == target and len(sequence) > 2):
            sequence.append(top := self.turn('N' if top % 2 else 'E'))
        sequence.append(self.turn('N' if top % 2 else 'E'))
        return sequence
