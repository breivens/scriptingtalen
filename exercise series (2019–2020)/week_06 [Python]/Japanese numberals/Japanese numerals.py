# noinspection Duplicates
class Japanese:
    numbers, units, exponents = '零一二三四五六七八九', '千百十', '万億兆京垓秭穣溝澗正載極'

    def __init__(self, value):
        assert (isinstance(value, int) and 0 <= value <= 10 ** 52) or (isinstance(value, str) and all(
            char in Japanese.numbers + Japanese.units + Japanese.exponents for char in value)), "invalid number"
        self.numeral = value if isinstance(value, str) else Japanese.toJapanese(value)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self}')"

    def __str__(self):
        return self.numeral

    def __int__(self):
        return Japanese.fromJapanese(self.numeral)

    def __add__(self, other):
        return Japanese(int(self) + int(other))

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Japanese(int(self) - int(other))

    def __rsub__(self, other):
        return Japanese(other).__sub__(self)

    def __mul__(self, other):
        return Japanese(int(self) * int(other))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __floordiv__(self, other):
        return Japanese(int(self) // int(other))

    def __rfloordiv__(self, other):
        return Japanese(other).__floordiv__(self)

    def __mod__(self, other):
        return Japanese(int(self) % int(other))

    def __rmod__(self, other):
        return Japanese(other).__mod__(self)

    def __pow__(self, other):
        return Japanese(int(self) ** int(other))

    def __rpow__(self, other):
        return Japanese(other).__pow__(self)

    def __eq__(self, other):
        return int(self) == int(other)

    def __ne__(self, other):
        return int(self) != int(other)

    def __lt__(self, other):
        return int(self) < int(other)

    def __le__(self, other):
        return int(self) <= int(other)

    def __gt__(self, other):
        return int(self) > int(other)

    def __ge__(self, other):
        return int(self) >= int(other)

    @staticmethod
    def split_myriads(integer):
        length = len(integer := str(integer))
        length = length if length % 4 == 0 else (length // 4 + 1) * 4
        return list(map("".join, zip(*[iter(integer.zfill(length))] * 4)))

    @staticmethod
    def myriad(digits):
        myr = ""
        if digits == '0000':
            return '零'
        for c, char in enumerate(digits):
            char = int(char)
            if (char == 1 and c == 3) or char > 1:
                myr += Japanese.numbers[1:][char - 1]
            if char > 0 and c < 3:
                myr += Japanese.units[c]
        return myr

    @staticmethod
    def toJapanese(integer):
        myriads, string = Japanese.split_myriads(integer), ""
        for m, myr in enumerate(myriads):
            if myr == '0000' and myriads != ['0000']:
                continue
            string += Japanese.myriad(myr)
            if (exp := len(myriads) - m - 2) > -1:
                string += Japanese.exponents[exp]
        return string

    @staticmethod
    def fromJapanese(numerals):
        num, myr, integer = 0, 0, 0
        for char in numerals:
            if char in Japanese.numbers:
                num = Japanese.numbers.index(char)
            elif char in Japanese.units:
                myr += (1 if num == 0 else num) * 10 ** (3 - Japanese.units.index(char))
                num = 0
            elif char in Japanese.exponents:
                integer += (myr + num) * 10 ** (4 * (Japanese.exponents.index(char) + 1))
                num, myr = 0, 0
        return integer + myr + num
