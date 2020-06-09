class Maya:
    def __init__(self, numeral: str):
        from re import match
        assert (isinstance(numeral, str)
                and all(
                    num == 'S' or (0 < len(num) < 9 and match(r"^[.]{0,4}[-]{0,3}$", num)) for num in numeral.split())
                and numeral == Maya.to_mayan(Maya.from_mayan(numeral))), "invalid maya number"
        self.numeral = numeral

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.numeral}')"

    def __str__(self):
        return self.numeral

    def __int__(self):
        return Maya.from_mayan(self.numeral)

    def __add__(self, other):
        return Maya(Maya.to_mayan(int(self) + int(other)))

    def __sub__(self, other):
        return Maya(Maya.to_mayan(int(self) - int(other)))

    def __mul__(self, other):
        return Maya(Maya.to_mayan(int(self) * int(other)))

    def __mod__(self, other):
        return Maya(Maya.to_mayan(int(self) % int(other)))

    def __floordiv__(self, other):
        return Maya(Maya.to_mayan(int(self) // int(other)))

    @staticmethod
    def from_mayan(numeral: str):
        numeral = reversed([num.count('.') + num.count('-') * 5 for num in numeral.split()])
        return int(sum(num * 20 ** n if n < 2 else num * 360 * 20 ** (n - 2) for n, num in enumerate(numeral)))

    @staticmethod
    def to_mayan(integer: int):
        assert integer > 0, "invalid maya number"
        if integer == 0:
            return 'S'
        n, numeral = 0, list()
        while integer > 360 * 20 ** n:
            n += 1
        for i in range(n + 1, -1, -1):
            if i < 2:
                num = integer // 20 ** i
                integer -= num * 20 ** i
            else:
                num = integer // (360 * 20 ** (i - 2))
                integer -= num * 360 * 20 ** (i - 2)
            numeral.append(num)
        return " ".join(['S' if num == 0 else num % 5 * '.' + num // 5 * '-' for num in numeral]).strip('S ')
