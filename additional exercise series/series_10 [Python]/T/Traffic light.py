class TrafficLight:
    states = ('green', 'orange', 'red')

    def __init__(self, state='red'):
        self.state = TrafficLight.states.index(state)

    def __repr__(self):
        return f"{self.__class__.__name__}({TrafficLight.states[self.state]!r})"

    def __str__(self):
        return TrafficLight.states[self.state]

    def next(self):
        self.state = (self.state + 1) % 3
