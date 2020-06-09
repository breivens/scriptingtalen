class OdoMeter:
    def __init__(self, distance=0.0, unit=True):
        self.distance = float(distance)
        self.unit = unit

    def __repr__(self):
        return f"{self.__class__.__name__}({self.distance:.6f}, {self.unit})"

    def __str__(self):
        return f"{self.distance:.1f} {'km' if self.unit else 'mi'}"

    def __add__(self, other):
        self.distance += other
        return self

    def __sub__(self, other):
        self.distance = max(self.distance - other, 0)
        return self

    def switch(self):
        self.distance *= 1 / 1.609344 if self.unit else 1.609344
        self.unit = not self.unit
