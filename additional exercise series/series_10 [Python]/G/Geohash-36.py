from string import ascii_letters as letters


class Geohash36:
    default = '23456789bBCdDFgGhHjJKlLMnNPqQrRtTVWX'

    def __init__(self, code: str, alphabet=default):
        assert (len(alphabet) == len(set(alphabet)) == 36 and
                set(alphabet) <= set(letters + '0123465798')), "invalid alphabet"

        self.alphabet = alphabet
        self.code, self.checksum_letter = code.split('-') if '-' in code else (code, None)

        assert (set(self.code) <= set(self.alphabet) and
                self.checksum_letter in (self.checksum(), None)), "invalid code"

        self.checksum_letter = self.checksum_letter or self.checksum()

    def checksum(self):
        return letters[sum([(len(self.code) - c) * self.alphabet.index(char) for c, char in enumerate(self.code)]) % 26]

    def __str__(self):
        return f"{self.code}-{self.checksum_letter}"

    def __repr__(self):
        if self.alphabet == Geohash36.default:
            return f"{self.__class__.__name__}({str(self)!r})"
        return f"{self.__class__.__name__}({str(self)!r}, alphabet={str(self.alphabet)!r})"

    def position(self, symbol: str):
        assert symbol in self.alphabet, "invalid symbol"
        index = self.alphabet.index(symbol)
        return 5 - index // 6, index % 6

    def longitude(self):
        l, u = -180.0, 180.0
        for char in self.code:
            c = self.position(char)[1]
            l, u = l + c * (u - l) / 6, l + (c + 1) * (u - l) / 6
        return l, u

    def latitude(self):
        l, u = -90.0, 90.0
        for char in self.code:
            r = self.position(char)[0]
            l, u = l + r * (u - l) / 6, l + (r + 1) * (u - l) / 6
        return l, u

    def coordinates(self):
        return sum(self.longitude()) / 2, sum(self.latitude()) / 2
