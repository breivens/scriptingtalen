class LFSR:
    def __init__(self, seed, taps, xor=True):
        self.bitstring = seed
        self.taps = sorted((tap - 1 for tap in taps), reverse=True)  # tap - 1 to get index and reverse because R -> L
        self.xnor = not xor

    def __repr__(self):
        return self.bitstring

    def __index__(self):
        return int(self.bitstring, 2)

    def __next__(self):
        tbits = tuple(map(lambda t: int(self.bitstring[t]), self.taps))  # tap to corresponding bit in bitstring
        input_bit, output_bit = tbits[0], int(self.bitstring[-1])
        for i in range(1, len(tbits)):  # calculate input bit
            input_bit ^= tbits[i]
            if self.xnor:
                input_bit = 1 - input_bit

        self.bitstring = str(input_bit) + self.bitstring[:-1]  # create new bitstring
        return output_bit

    def states(self):
        states, shifts = set(), 0
        while self.bitstring not in states:
            shifts += 1
            states.add(self.bitstring)
            self.__next__()
        return shifts
