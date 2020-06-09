from itertools import zip_longest


class Polynomial:
    def __init__(self, sequence: list):
        self.coefficients = self.trim(sequence)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.coefficients})"

    def __str__(self):
        if self.coefficients:
            return " ".join([
                ('- ' if item < 0 else '+ ') +
                (str(abs(item)) * (not (abs(item) == 1 and i > 0))  # coefficient
                 + ' * x' * (i >= 1)  # variable
                 + f'^{i}' * (i >= 2)  # exponent
                 ).lstrip(' * ') for i, item in enumerate(self.coefficients) if item
            ]).lstrip('+ ')
        return '0'

    def __neg__(self):
        return Polynomial(list(map(int.__neg__, self.coefficients)))

    def __add__(self, other):
        return Polynomial([x + y for x, y in zip_longest(self.coefficients, other.coefficients, fillvalue=0)])

    def __sub__(self, other):
        return Polynomial([x - y for x, y in zip_longest(self.coefficients, other.coefficients, fillvalue=0)])

    def __mul__(self, other):
        return sum(
            map(Polynomial, [[0] * i + [x * y for y in other.coefficients] for i, x in enumerate(self.coefficients)]),
            start=Polynomial([0]))

    def derivative(self):
        return Polynomial([item * i for i, item in enumerate(self.coefficients)][1:])

    @staticmethod
    def trim(sequence: iter):
        if sequence[-1] == 0:
            for i, item in enumerate(reversed(sequence)):  # remove trailing zeroes
                if item:
                    return sequence[:-1 * i]
        return list() if set(sequence) == {0} else sequence
