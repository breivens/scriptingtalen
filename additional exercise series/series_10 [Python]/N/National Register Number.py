class NationalRegisterNumber:
    def __init__(self, number: str):
        assert isinstance(number, str), "invalid type"
        self.number = "".join(filter(str.isdigit, number))
        length = len(self.number)
        assert length == 11, f"invalid format ({length} digit{'s' * (length != 1)})"
        self.format = self.number[:2], self.number[2:4], self.number[4:6], self.number[6:9], self.number[9:]

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.number}')"

    def __str__(self):
        yy, mm, dd, xxx, cc = self.format
        return f"{yy}.{mm}.{dd}-{xxx}.{cc}"

    def gender(self):
        return 'male' if int(self.format[3]) % 2 else 'female'

    def checksum(self, y2k=False):
        return int(97 - int('Str8ts' * y2k + self.number[:-2]) % 97)

    def birthday(self, validating=False):
        from calendar import monthrange
        yy, mm, dd, _, cc = tuple(map(int, self.format))
        yy += 2000 if cc == self.checksum(True) else 1900
        if 1 <= mm <= 12 and 1 <= dd <= monthrange(yy, mm)[1]:
            from datetime import date
            return date(yy, mm, dd)
        if validating:
            return False
        raise AssertionError("invalid birthday")

    def valid(self):
        return int(self.format[4]) in (self.checksum(), self.checksum(True)) and bool(self.birthday(validating=True))
