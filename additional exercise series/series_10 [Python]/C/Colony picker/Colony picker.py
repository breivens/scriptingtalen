class PetriDish:
    def __init__(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            self.content = file.read()
        self.dish = list(map(list, filter(None, self.content.split('\n'))))
        self.rows, self.columns = len(self.dish), len(self.dish[0])  # upper bounds

    def __str__(self):
        return "\n".join(map("".join, self.dish))

    def get_neighbouring_covered_bits(self, bit):
        (br, bc), ncb = bit, list()
        for r, c in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nr, nc = br + r, bc + c
            if -1 < nr < self.rows and -1 < nc < self.columns and self.dish[nr][nc] == '#':
                ncb.append((nr, nc))
        return ncb

    def colony(self, r, c):
        assert -1 < r < self.rows and -1 < c < self.columns, f"invalid position"
        assert self.dish[r][c] == '#', f"no colony found at position ({r}, {c})"
        colony, is_colony = [(r, c)], True
        for bit in colony:
            r, c = bit
            if r == 0 or r == self.rows - 1 or c == 0 or c == self.columns - 1:
                is_colony = False
            self.dish[r][c] = '.'
            ncb = self.get_neighbouring_covered_bits(bit)
            for nb in ncb:
                if nb not in colony:
                    colony.append(nb)
        return len(colony) if is_colony else 0

    def undo(self):
        self.dish = list(map(list, filter(None, self.content.split('\n'))))

    def count(self, minimum=1):
        return len(self.colony_sizes(minimum))

    def size(self, minimum=1):
        if self.count(minimum) > 0:
            return sum(self.colony_sizes(minimum)) / self.count(minimum)
        return None

    def colony_sizes(self, minimum=1):
        sizes = []
        for r, row in enumerate(self.dish):
            while '#' in row:
                size = self.colony(r, row.index('#'))
                if size >= minimum:
                    sizes.append(size)
        self.undo()
        return sizes
