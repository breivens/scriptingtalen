class Playfair:
    def __init__(self, key: str):
        from string import ascii_uppercase
        self.grid = tuple(zip(*[iter(dict.fromkeys((key.upper() + ascii_uppercase).replace("J", "I")))] * 5))

    def __str__(self):
        return "\n".join(map("".join, self.grid))

    def digraph(self, digraph: str, encode=True):
        digraph = digraph.upper()
        assert len(digraph) == 2 and digraph[0] != digraph[1], "two different letters required"
        offset = 1 if encode else -1
        (r1, c1), (r2, c2) = ((r, row.index(char)) for char in digraph
                              for r, row in enumerate(self.grid) if char in row)
        if r1 == r2:
            return self.grid[r1][(c1 + offset) % 5] + self.grid[r2][(c2 + offset) % 5]
        if c1 == c2:
            return self.grid[(r1 + offset) % 5][c1] + self.grid[(r2 + offset) % 5][c2]
        return self.grid[r1][c2] + self.grid[r2][c1]

    def encode(self, plaintext: str):
        encoded, plaintext = "", "".join(filter(str.isalpha, plaintext.upper()))
        while plaintext:
            digraph, plaintext = plaintext[:2], plaintext[2:]
            if len(digraph) == 1:
                digraph += 'Q' if digraph == 'X' else 'X'
            if digraph[0] == digraph[1]:
                digraph, plaintext = digraph[0] + ('Q' if digraph == 'XX' else 'X'), digraph[1] + plaintext
            encoded += self.digraph(digraph)
        return encoded

    def decode(self, encoded: str):
        return "".join([self.digraph(encoded[i:i + 2], False) for i in range(0, len(encoded), 2)])

    # --- alternatives --- #
    def decode_alt_for(self, encoded: str):
        return "".join([self.digraph("".join(digraph), False) for digraph in zip(*[iter(encoded)] * 2)])

    def decode_alt_while(self, encoded: str):
        decoded = ""
        while encoded:
            decoded += self.digraph(encoded[:2], False)
            encoded = encoded[2:]
        return decoded
