from datetime import datetime, timedelta


class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        assert 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60, "invalid time"
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def __repr__(self):
        return f"{self.__class__.__name__}{self.hours, self.minutes, self.seconds}"

    def __str__(self):
        return ":".join(str(t).zfill(2) for t in (self.hours, self.minutes, self.seconds))

    def set(self, hours=0, minutes=0, seconds=0):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def forward(self, hours=0, minutes=0, seconds=0):
        current = datetime.strptime(str(self), "%H:%M:%S") + timedelta(hours=hours, minutes=minutes, seconds=seconds)
        self.hours, self.minutes, self.seconds = current.hour, current.minute, current.second


clock = Clock(hours=5)
print(repr(clock))
print(clock)