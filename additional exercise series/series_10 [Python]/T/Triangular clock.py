class Clock:
    def __init__(self, h: int, m: int):
        assert 0 <= h <= 23 and 0 <= m <= 59, "invalid time"
        self.hours = h
        self.minutes = m

    def __repr__(self):
        return f"{self.__class__.__name__}{self.hours, self.minutes}"

    def __str__(self):
        triangle, color = self.lamps()
        length = len(triangle)
        return "\n".join(
            [" ".join((color * lamp).ljust(i + 1, '.')).rjust(i + length)
             for i, lamp in enumerate(triangle)])

    def updateHours(self, h=1):
        self.hours += h
        if self.hours > 23:
            self.hours %= 24
        if self.hours < 0:
            self.hours %= 24
        return self

    def updateMinutes(self, m=1):
        self.minutes += m
        if self.minutes > 59:
            self.updateHours(self.minutes // 60)
            self.minutes %= 60
        if self.minutes < 0:
            self.updateHours(self.minutes // 60)
            self.minutes %= 60
        return self

    def lamps(self):
        time = self.hours % 12 * 60 + self.minutes
        triangle = list()
        for div in (360, 120, 30, 6):
            triangle.append(time // div)
            time %= div
        triangle.append(time)
        return tuple(triangle), 'R' if self.hours // 12 else 'G'


clock = Clock(11, 3)
print(clock)
