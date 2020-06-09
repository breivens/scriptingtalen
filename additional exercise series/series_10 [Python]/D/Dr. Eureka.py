class Eureka:
    def __init__(self, configuration: str, maximum=4, flipped=None):
        self.config = configuration.split(',')
        self.tube_count = len(self.config)
        assert (all(len(tube) <= maximum for tube in self.config)
                and (flipped is None or -1 < flipped < self.tube_count)), 'invalid configuration'
        self.max = maximum
        self.flipped = flipped

    def __repr__(self):
        config = ','.join(self.config)
        flipped = '' if self.flipped is None else f', flipped={self.flipped}'
        return f'{self.__class__.__name__}({config!r}, maximum={self.max}{flipped})'

    def __str__(self):
        tubes = list(zip(*[tube.ljust(self.max) for tube in self.config]))[::-1]  # arrange ball order
        tubes = [[f'|{t}|' for t in tube] for tube in tubes]  # format balls in tube
        tubes = [['= ='] * self.tube_count] + tubes + [['==='] * self.tube_count]  # add top and bottom of tube
        if self.flipped is not None:  # switch top and bottom if necessary
            tubes[0][self.flipped], tubes[-1][self.flipped] = tubes[-1][self.flipped], tubes[0][self.flipped]
        return '\n'.join(map(' '.join, tubes))

    def __eq__(self, other):
        return set(self.config) == set(other.config)

    def flip(self, index: int):
        assert -1 < index < self.tube_count and self.flipped in (None, index), 'invalid move'
        self.flipped = None if index == self.flipped else index
        self.config[index] = self.config[index][::-1]
        return self

    def transfer(self, source: int, destination: int, count=None):
        count = count or len(self.config[source])
        assert (source != destination
                and -1 < source < self.tube_count
                and -1 < destination < self.tube_count
                and self.flipped is None
                and len(self.config[destination]) + count <= self.max), 'invalid move'
        self.config[source], balls = self.config[source][:-count], self.config[source][-count:][::-1]
        self.config[destination] += balls
        return self
