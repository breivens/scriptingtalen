class Block:
    def __init__(self, length: int, height: int, width: int, position=(0, 0)):
        self.L = length
        self.H = height
        self.W = width
        self.pos = list(position)

    def __repr__(self):
        return f"{self.__class__.__name__}(length={self.L}, height={self.H}, width={self.W}, position={tuple(self.pos)})"

    def area(self):
        return float(2 * (self.L * self.W + self.L * self.H + self.H * self.W))

    def volume(self):
        return float(self.L * self.H * self.W)

    def diagonal(self):
        return float((self.L ** 2 + self.H ** 2 + self.W ** 2) ** .5)

    def slide(self, direction: str):
        assert direction in ('F', 'B', 'R', 'L'), "invalid direction"
        self.pos[0] += self.W * (1 if direction == 'F' else -1 if direction == 'B' else 0)
        self.pos[1] += self.L * (1 if direction == 'R' else -1 if direction == 'L' else 0)
        return self

    def tilt(self, direction: str):
        assert direction in ('F', 'B', 'R', 'L'), "invalid direction"
        if direction in 'FB':
            self.pos[0] += self.H if direction == 'F' else -self.W
            self.H, self.W = self.W, self.H
        elif direction in 'RL':
            self.pos[1] += self.L if direction == 'R' else -self.H
            self.L, self.H = self.H, self.L
        return self

    def sail(self, string: str):
        for move, direction in zip(*[iter(string)] * 2):
            if move == 'S':
                self.slide(direction)
            elif move == 'T':
                self.tilt(direction)
            else:
                raise AssertionError("invalid movement")
        return self
