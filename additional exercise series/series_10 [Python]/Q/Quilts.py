class Quilt:
    def __init__(self, rows: int, columns: int, pattern: str):
        assert rows * columns == len(pattern) and set(pattern) <= set('\\/+*-|ox'), "invalid configuration"
        self.rows, self.columns, self.pattern = rows, columns, pattern

    def __repr__(self):
        return f"{self.__class__.__name__}{self.rows, self.columns, self.pattern}"

    def __str__(self):
        return '\n'.join(map(''.join, self.patch))

    def __add__(self, other):
        assert self.rows == other.rows, "quilts do not have an equal height"
        pattern = ''.join([''.join(x + y) for x, y in zip(self.patch, other.patch)])
        return Quilt(self.rows, self.columns + other.columns, pattern)

    @property
    def patch(self):
        return list(map(list, zip(*[iter(self.pattern)] * self.columns)))

    def rotate(self):
        from numpy import array, rot90
        pattern = ''.join(map(''.join, rot90(array(self.patch), 3)))
        return Quilt(self.columns, self.rows, pattern.translate(str.maketrans('\\/-|', '/\\|-')))
