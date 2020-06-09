class Conway:
    def __init__(self, number: int):
        self.num = number

    def __next__(self):
        from itertools import groupby
        groups = ["".join(group) for _, group in groupby(str(self.num))]
        self.num = int("".join([f"{len(group)}{group[0]}" for group in groups]))
        return self.num
