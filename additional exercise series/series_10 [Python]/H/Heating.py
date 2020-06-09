class Heater:
    def __init__(self, name: str, temperature=10.0, minimum=0.0, maximum=100.0):
        self.name = name
        self.temp = float(temperature)
        self.min = float(minimum)
        self.max = float(maximum)

    def __str__(self):
        return f"{self.name}: current temperature: {self.temp}; allowed min: {self.min}; allowed max: {self.max}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.temp:.1f}, {self.min:.1f}, {self.max:.1f})"

    def change_temperature(self, t: int or float):
        self.temp = min(max(self.temp + t, self.min), self.max)

    def temperature(self):
        return self.temp


machine1 = Heater('radiator kitchen', temperature=20.0)
print(machine1)
print()
machine2 = Heater('radiator living', minimum=15, temperature=18)
print(machine2)
print()
machine3 = Heater('radiator bathroom', temperature=22, minimum=18, maximum=28)
print(machine3)
