from math import gcd


class Beaufort:
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return self.key[:2] + '*' * (len(self.key) - 4) + self.key[-2:]

    def __repr__(self):
        return f"Beaufort('{self.key}')"

    def __add__(self, other, sign=1):
        return Beaufort.get_new_key(self, other, 1)

    def __sub__(self, other):
        return Beaufort.get_new_key(self, other, -1)

    def __mul__(self, other):
        return Beaufort("".join(chr(((ord(self.key[i]) - 65) * other % 26) + 65) for i in range(len(self.key))))

    def __rmul__(self, other):
        return self.__mul__(other)

    def get_new_key(self, other, sign):
        len1, len2 = len(self.key), len(other.key)
        lcm = len1 * len2 // gcd(len1, len2)
        key1, key2 = self.key * (lcm // len1), other.key * (lcm // len2)
        new_key = "".join(chr((((ord(key1[i]) - 65) + sign * (ord(key2[i]) - 65)) % 26) + 65) for i in range(lcm))
        return Beaufort(new_key)

    def encode_letter(self, letter, index):
        return chr((((ord(self.key[index % len(self.key)]) - 65) - (ord(letter) - 65)) % 26) + 65)

    def encode(self, line):
        output = ""
        for c, char in enumerate(line):
            output += self.encode_letter(char, c)
        return output

    def decode_letter(self, letter, index):
        return self.encode_letter(letter, index)

    def decode(self, line):
        return self.encode(line)
