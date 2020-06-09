class Molecule:
    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self.grid = [['.'] * columns for _ in range(rows)]

    def __str__(self):
        return '\n'.join(map(' '.join, self.grid))

    def atom(self, position, forward=True):
        r, c = position
        assert -1 < r < self.rows and -1 < c < self.columns and self.grid[r][c] == '.', "invalid position"
        self.grid[r][c] = '/' if forward else '\\'

    def atoms(self, atoms: tuple, forward=True):
        for atom in atoms:
            self.atom(atom, forward)

    def simulate_beam(self, position: tuple, direction: str):
        directions = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
        path = [position]
        while position:
            r, c = path[-1]
            direction = {
                '/': {'N': 'E', 'E': 'N', 'S': 'W', 'W': 'S'}[direction],
                '\\': {'N': 'W', 'W': 'N', 'S': 'E', 'E': 'S'}[direction]
            }.get(self.grid[r][c], direction)

            dx, dy = directions[direction]
            r, c = r + dx, c + dy

            if -1 < r < self.rows and -1 < c < self.columns:
                path.append((r, c))
            else:
                position = None
        return path, direction

    def deflection(self, position: tuple, direction: str):
        return self.simulate_beam(position, direction)[0]

    def diffraction(self, position: tuple, direction: str):
        path, direction = self.simulate_beam(position, direction)
        return path[-1], direction
