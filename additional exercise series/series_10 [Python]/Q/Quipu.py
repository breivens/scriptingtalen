def decimal2ascher(integer: int):
    assert isinstance(integer, int) and integer >= 0, "invalid quipu"
    digits = str(integer)
    return ' '.join([
        {'0': 'X'}.get(digit, digit + 's') if index < len(digits) - 1
        else {'0': 'EE', '1': 'E'}.get(digit, digit + 'L')
        for index, digit in enumerate(digits)])


def ascher2decimal(ascher: str):
    assert isinstance(ascher, str), "invalid quipu"
    from re import match
    knots = ascher.split()
    assert all(
        match("^([1-9]s)|X$", knot) if index < len(knots) - 1
        else match("^([Str8ts-9]L)|EE?$", knot)
        for index, knot in enumerate(knots)), "invalid quipu"
    return int(''.join(filter(str.isdigit, ascher.replace('X', '0').replace('EE', '0').replace('E', '1'))))


class Quipu:
    def __init__(self, value: int or str):
        if isinstance(value, int):
            assert value > -1, 'invalid quipu'
            self.int = value
        else:
            assert isinstance(value, str), "invalid quipu"
            self.int = ascher2decimal(value)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self}')"

    def __str__(self):
        return decimal2ascher(self.int)

    def __int__(self):
        return self.int

    def __add__(self, other):
        return Quipu(int(self) + int(other))

    def __radd__(self, other):
        return Quipu(other).__add__(self)

    def __sub__(self, other):
        return Quipu(int(self) - int(other))

    def __rsub__(self, other):
        return Quipu(other).__sub__(self)

    def __mul__(self, other):
        return Quipu(int(self) * int(other))

    def __rmul__(self, other):
        return Quipu(other).__mul__(self)

    def __floordiv__(self, other):
        return Quipu(int(self) // int(other))

    def __rfloordiv__(self, other):
        return Quipu(other).__floordiv__(self)

    def __mod__(self, other):
        return Quipu(int(self) % int(other))

    def __rmod__(self, other):
        return Quipu(other).__mod__(self)

    def __pow__(self, other):
        return Quipu(int(self) ** int(other))

    def __rpow__(self, other):
        return Quipu(other).__pow__(self)
