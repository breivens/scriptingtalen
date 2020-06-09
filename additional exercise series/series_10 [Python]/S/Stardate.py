import datetime


class Stardate:
    def __init__(self, staredate=datetime.date.today()):
        self.stardate = staredate
        self.new = True

    def __repr__(self):
        return f"{self.__class__.__name__}({self.stardate!r})"

    def __str__(self):
        year = self.stardate.year
        if self.new:
            from calendar import isleap
            delta = (self.stardate - datetime.date(year, 1, 1)).days
            fraction = delta * 100 // (366 if isleap(year) else 365)
            return f"{year}.{str(fraction).zfill(2)}"
        delta = (year - 1900) // 100
        return str(delta) * (delta > 0) + self.stardate.strftime(f"%y%m.%d")

    def switch(self):
        self.new = not self.new

