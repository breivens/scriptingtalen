class Mangarevan:
    def __init__(self, value: int or str):
        assert (isinstance(value, int) and 0 < value < 800) or (
                isinstance(value, str) and self.validate(value)), "invalid value"
        self.value = value if isinstance(value, str) else Mangarevan.to_mangarevan(value)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self}')"

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return self.from_mangarevan(self.value)

    def __add__(self, other):
        return Mangarevan(int(self) + int(other))

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Mangarevan(int(self) - int(other))

    def __rsub__(self, other):
        return Mangarevan(other).__sub__(self)

    def __mul__(self, other):
        return Mangarevan(int(self) * int(other))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __floordiv__(self, other):
        return Mangarevan(int(self) // int(other))

    def __rfloordiv__(self, other):
        return Mangarevan(other).__floordiv__(self)

    def __mod__(self, other):
        return Mangarevan(int(self) % int(other))

    def __rmod__(self, other):
        return Mangarevan(other).__mod__(self)

    def __pow__(self, other):
        return Mangarevan(int(self) ** int(other))

    def __rpow__(self, other):
        return Mangarevan(other).__pow__(self)

    @staticmethod
    def validate(string: str):
        if string.isdigit() and len(string) == 1:
            return True
        for c, char in enumerate(string):
            if c == 0:
                if (char.isdigit() and string[1] != 'V') and char not in 'VTPK':
                    return False
            elif c == len(string) - 1:
                if not char.isdigit and char not in 'VTPK':
                    return False
            elif char not in 'VTPK':
                return False
        return True

    @staticmethod
    def from_mangarevan(string: str):
        if string.isdigit():
            return int(string)
        return sum({'V': (int(string[0]) if string[0].isdigit() else 1) * 80, 'T': 40, 'P': 20, 'K': 10}.get(char, 0)
                   for char in string) + (int(string[-1]) if string[-1].isdigit() else 0)

    @staticmethod
    def to_mangarevan(integer: int):
        factors = list()
        for i in range(3, -1, -1):
            num = 10 * 2 ** i
            a = integer // num
            integer -= a * num
            factors.append(a)
        return "".join([f"{factor}V" if i == 0 and factor != 0 else factor * 'VTPK'[i]
                        for i, factor in enumerate(factors)]) + ("" if integer == 0 else str(integer))

