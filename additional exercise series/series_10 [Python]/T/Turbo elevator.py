class Platform:
    DOWN, STILL, UP = -1, 0, 1

    def __init__(self, state: int, direction: int, lowest=None, highest=None):
        self.state = state
        self.direction = direction
        self.lowest = lowest if lowest is not None else state
        self.highest = highest if highest is not None else state
        assert (self.lowest <= self.state <= self.highest and
                direction in {Platform.DOWN, Platform.STILL, Platform.UP}), "invalid configuration"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.state, self.direction, self.lowest, self.highest}"

    def __eq__(self, other):
        return self.state == other.state

    def next(self):
        if self.lowest != self.highest:
            self.direction = {self.lowest: Platform.UP, self.highest: Platform.DOWN}.get(self.state, self.direction)
            self.state += self.direction


class TurboElevator:
    def __init__(self):
        self.platforms = list()
        self.count = 0

    def add(self, platform: Platform):
        self.platforms.append(platform)
        self.count += 1

    def next(self):
        for i in range(self.count):
            self.platforms[i].next()

    def timesteps(self):
        i = steps = 0
        for _ in range(1000):
            self.next()
            i += self.platforms[i] == self.platforms[i + 1]
            steps += 1
            if i == self.count - 1:
                return steps
        return None
