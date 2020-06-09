from math import gcd


class T52:
    def __init__(self, a: int, b: int, alphabet: str):
        self.m = len(alphabet)
        assert len(set(alphabet)) == self.m, "alphabet has repeated symbols"
        assert gcd(a, self.m) == 1, f"{a} and {self.m} are not coprime"
        self.a, self.b, self.alphabet = a, b, alphabet

    def __add__(self, other):
        assert self.alphabet == other.alphabet, "alphabets are different"
        return T52(self.a * other.a, other.a * self.b + other.b, self.alphabet)

    def encodeSymbol(self, symbol: str):
        if symbol in self.alphabet:
            return self.alphabet[(self.a * self.alphabet.index(symbol) + self.b) % self.m]
        return symbol

    def decodeSymbol(self, symbol: str):
        if symbol in self.alphabet:
            return self.alphabet[self.inv_mod(self.a, self.m) * (self.alphabet.index(symbol) - self.b) % self.m]
        return symbol

    def encode(self, message: str):
        return "".join([self.encodeSymbol(s) for s in message])

    def decode(self, message: str):
        return "".join([self.decodeSymbol(s) for s in message])

    @staticmethod
    def inv_mod(a: int, m: int):
        for n in range(m):
            if a * n % m == 1:
                return n
        return 1


machine1 = T52(3, 5, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
machine2 = T52(17, 11, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(machine2.encode(machine1.encode('G-SCHREIBER')))
machine12 = machine1 + machine2
print(machine12.encode("G-SCHREIBER"))
