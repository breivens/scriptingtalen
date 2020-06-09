class Sequence:
    def __init__(self, sequence: str):
        self.seq = sequence.upper()
        assert self.validate(), "invalid sequence"

    def validate(self):
        return set(self.seq) <= set('ACTG')

    def distance(self, other):
        n, m = len(self.seq) + 1, len(other.seq) + 1
        matrix = [[j if i == 0 else i if j == 0 else 0 for j in range(m)] for i in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                matrix[i][j] = min(matrix[i - 1][j] + 1,
                                   matrix[i][j - 1] + 1,
                                   matrix[i - 1][j - 1] + (0 if self.seq[i - 1] == other.seq[j - 1] else 1))
        return matrix[-1][-1]
