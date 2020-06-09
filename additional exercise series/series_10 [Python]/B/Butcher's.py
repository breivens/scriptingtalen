class NumberSystem:
    def __init__(self, current=0, last=0):
        self.current = current
        self.last = last

    def __str__(self):
        return f"Current client: {self.current}, last ticket: {self.last}"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.current, self.last}"

    def currentClient(self):
        return self.current

    def takeNumber(self):
        temp = self.last + 1
        if self.current > self.last and temp < self.current:
            self.last = 1 if temp == 100 else temp
            return self.last
        if temp > self.current:
            self.last = 1 if temp == 100 else temp
            return self.last
        return None

    def nextClient(self):
        temp = self.current + 1
        if self.current > self.last and temp >= self.last:
            self.current = 1 if temp == 100 else temp
        elif temp <= self.last:
            self.current = 1 if temp == 100 else temp


number = NumberSystem(15, 12)
print(repr(number))


