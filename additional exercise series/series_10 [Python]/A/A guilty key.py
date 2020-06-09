class Cipher:
    def __init__(self, keyword, description):
        self.key = keyword
        self.desc = description
        self.grid = self._construct_grid()
        self.map = self._construct_map()

    def _construct_grid(self):
        from re import sub
        size = len(self.key)
        temp = sub('[0-9]+', lambda l: int(l.group(0)) * '-', self.desc).ljust(size ** 2, '-')
        return list(map(list, zip(*[iter(temp)] * size)))

    def _construct_map(self):
        output = {}
        for r, row in enumerate(self.grid):
            for c, column in enumerate(row):
                if column.isalpha():
                    output[column] = self.key[r] + self.key[c]
        return output

    def encode(self, string):
        assert set(filter(str.isalpha, string.upper())) <= set(self.desc), 'invalid message'
        return ''.join(map(lambda l: self.map.get(l, ""), string.upper()))

    def decode(self, string):
        groups = list(map(''.join, zip(*[iter(string)] * 2)))
        assert len(string) % 2 == 0 and set(groups) <= set(self.map.values()), 'invalid message'
        keymap = {v: k for k, v in self.map.items()}
        return ''.join(map(lambda l: keymap[l], groups))
