class DotPlot:
    def __init__(self, sequence1: str, sequence2: str):
        self.sequence1 = sequence1
        self.sequence2 = sequence2

    def windows(self, start1: int, start2: int, length=1):
        assert start1 >= 0 and start2 >= 0 and length > 0, "invalid window size"
        assert start1 + length <= len(self.sequence1) and start2 + length <= len(
            self.sequence2), f"invalid start position"
        return self.sequence1[start1:start1 + length], self.sequence2[start2:start2 + length]

    def equal(self, start1: int, start2: int, length=1, number=1):
        window1, window2 = self.windows(start1, start2, length)
        return number <= sum(1 for i in range(length) if window1[i].lower() == window2[i].lower())

    def plot(self, length=1, step=None, number=1):
        step = step or length
        return [[self.equal(i, j, length, number) for j in range(0, len(self.sequence2) - length + 1, step)]
                for i in range(0, len(self.sequence1) - length + 1, step)]
