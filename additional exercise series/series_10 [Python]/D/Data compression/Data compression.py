from csv import reader


class ZIP:
    def __init__(self, path):
        with open(path, "r") as file:
            self.symbols = dict(reader(file, delimiter='\t'))
            self.bitstrings = {v: k for k, v in self.symbols.items()}

    def symbol2bitstring(self, symbol: str):
        assert symbol in self.symbols, f'unknown symbol "{symbol}"'
        return self.symbols[symbol]

    def bitstring2symbol(self, bitstring: str):
        assert bitstring in self.bitstrings, "invalid bitstring"
        return self.bitstrings[bitstring]

    def compress(self, string: str):
        return "".join(self.symbol2bitstring(symbol) for symbol in string)

    def decompress(self, bitstring: str):
        decompressed = ""
        lower_bound, upper_bound = len(min(self.bitstrings, key=len)), len(max(self.bitstrings, key=len))
        i = lower_bound
        while bitstring:
            if bitstring[:i] in self.bitstrings:
                decompressed += self.bitstring2symbol(bitstring[:i])
                bitstring, i = bitstring[i:], lower_bound
            else:
                assert i < upper_bound, "invalid bitstring"
                i += 1
        return decompressed
