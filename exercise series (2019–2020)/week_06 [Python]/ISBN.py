class ISBN13:
    def __init__(self, code, length=1):
        assert isinstance(code, int), "invalid ISBN code"
        assert 1 <= length <= 5, "invalid ISBN code"
        self.code = str(code)
        self.length = length

    def __str__(self):
        return f"{self.code[:3]}-{self.code[3:3 + self.length]}-{self.code[3 + self.length:-1]}-{self.code[-1]}"

    def __repr__(self):
        return f"ISBN13({int(self.code)}, {self.length})"

    def isvalid(self):
        ctrl = sum(int(self.code[i]) * (3 if i % 2 else 1) for i in range(12))
        return str((10 - (ctrl % 10)) % 10) == self.code[12]

    def asISBN10(self):
        if not self.isvalid() or str(self.code)[:3] != '978':
            return None
        code = self.code[3:-1]
        ctrl = sum(int(code[i]) * (i + 1) for i in range(9)) % 11
        x10 = "X" if ctrl == 10 else str(ctrl)
        return f"{code[:self.length]}-{code[self.length:]}-{x10}"
