class Mengenlehreuhr:
    def __init__(self, h: int, m: int):
        assert isinstance(h, int) and 0 <= h <= 23 and isinstance(m, int) and 0 <= m <= 59, "invalid time"
        self.hours = h
        self.minutes = m

    def __repr__(self):
        return f"{self.__class__.__name__}{self.hours, self.minutes}"

    def __str__(self):
        return '\n'.join(
            [(' #' * count + ' -' * (11 - count))[1:] if row == 2 else ' ####' * count + ' ----' * (4 - count)
             for row, count in enumerate(self.lamps())])

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
        return self.hours // 5, self.hours % 5, self.minutes // 5, self.minutes % 5


clock01 = Mengenlehreuhr(8, 25)
print(repr(clock01.updateMinutes(-56).updateMinutes(-38).updateMinutes(39)))
