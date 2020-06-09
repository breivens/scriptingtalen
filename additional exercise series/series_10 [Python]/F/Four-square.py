class Square:
    def __init__(self, keyword=''):
        self.keyword = keyword.upper()
        plaintext = ''
        for letter in self.keyword.upper() + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if letter not in plaintext + 'J':
                plaintext += letter
        self.grid = list(zip(*[iter(plaintext)] * 5))

    def __str__(self):
        return "\n".join(map(" ".join, self.grid))

    def letter(self, r: int, c: int):
        assert -1 < r < 5 and -1 < c < 5, "invalid position"
        return self.grid[r][c]

    def position(self, letter: str):
        letter = letter.upper().replace('J', 'I')
        for r, row in enumerate(self.grid):
            if letter in row:
                return r, row.index(letter)
        raise AssertionError("invalid letter")


class FourSquare:
    def __init__(self, keyword1: str, keyword2: str):
        self.square0 = Square()
        self.square1 = Square(keyword1)
        self.square2 = Square(keyword2)

    def encode(self, plaintext: str):
        digraphs = zip(*[iter("".join(filter(str.isalpha, plaintext + 'Q')).replace('J', 'I').upper())] * 2)
        encoded = ""
        for letter1, letter2 in digraphs:
            r1, c1 = self.square0.position(letter1)
            r2, c2 = self.square0.position(letter2)
            encoded += self.square1.letter(r1, c2) + self.square2.letter(r2, c1)
        return encoded

    def decode(self, encoded: str):
        digraphs = zip(*[iter("".join(filter(str.isalpha, encoded)).upper())] * 2)
        decoded = ""
        for letter1, letter2 in digraphs:
            r1, c1 = self.square1.position(letter1)
            r2, c2 = self.square2.position(letter2)
            decoded += self.square0.letter(r1, c2) + self.square0.letter(r2, c1)
        return decoded

    # slower alternatives
    def encode_alt(self, plaintext: str):
        plaintext = "".join(filter(str.isalpha, plaintext)).replace('J', 'I').upper()
        plaintext, encoded = plaintext + len(plaintext) % 2 * 'Q', ""
        while plaintext:
            r1, c1 = self.square0.position(plaintext[0])
            r2, c2 = self.square0.position(plaintext[1])
            encoded += self.square1.letter(r1, c2) + self.square2.letter(r2, c1)
            plaintext = plaintext[2:]
        return encoded

    def decode_alt(self, encoded: str):
        plaintext = "".join(filter(str.isalpha, encoded)).upper()
        decoded = ""
        while plaintext:
            r1, c1 = self.square1.position(plaintext[0])
            r2, c2 = self.square2.position(plaintext[1])
            decoded += self.square0.letter(r1, c2) + self.square0.letter(r2, c1)
            plaintext = plaintext[2:]
        return decoded


# "".join(c for c in s if c.isalpha()) vs "".join([c for c in s if c.isalpha()]) vs "".join(filter(str.isalpha, s)) test
# slowest - middle - fastest

square = Square()
print(square)