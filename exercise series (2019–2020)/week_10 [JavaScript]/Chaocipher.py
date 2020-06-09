class Disk:
    def __init__(self, alphabet: str):
        from string import ascii_uppercase
        self.alphabet = alphabet.upper()
        assert ''.join(sorted(self.alphabet)) == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "invalid alphabet"

    def __str__(self):
        return "".join(self.alphabet)

    def locate(self, letter: str):
        return self.alphabet.index(letter.upper()) + 1

    def letter(self, index: int):
        return self.alphabet[index - 1]

    def rotate(self, count: int):
        count = ((count % 26) + 26) % 26
        self.alphabet = self.alphabet[count:] + self.alphabet[:count]
        return self

    def roll(self, start: int, stop: int):
        self.alphabet = (self.alphabet[:start - 1]
                         + self.alphabet[start:stop]
                         + self.alphabet[start - 1]
                         + self.alphabet[stop:])
        return self


class Chaocipher:
    def __init__(self, left_alphabet: str, right_alphabet):
        self.left = Disk(left_alphabet)
        self.right = Disk(right_alphabet)

    def __str__(self):
        return f"""            +            *
 LEFT (ct): {self.left}
RIGHT (pt): {self.right}
            --------------------------"
  Position: 12345678911111111112222222"
                     01234567890123456"""

    def encode(self, plaintext: str):
        encoded = ""
        for letter in plaintext:
            index = self.right.locate(letter)
            encoded += self.left.letter(index)
            self.permute(index)
        return encoded

    def decode(self, encoded: str):
        decoded = ""
        for letter in encoded:
            index = self.left.locate(letter)
            decoded += self.right.letter(index)
            self.permute(index)
        return decoded

    def permute(self, index):
        self.left.rotate(index - 1).roll(2, 14)
        self.right.rotate(index).roll(3, 14)
