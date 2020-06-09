class PerfectMaze:
    def __init__(self, maze: str):
        self.data = [list(row) for row in maze.split('\n')]
        self.rows, self.columns = len(self.data), len(self.data[0])

    def __str__(self):
        return '\n'.join([f"{self.rows} x {self.columns} maze:"] + ["".join(row) for row in self.data])

    def getCell(self, t: tuple):
        x, y = t
        return self.data[x][y]

    def setCell(self, t: tuple, c: str):
        x, y = t
        self.data[x][y] = c

    def numberWalls(self, t: tuple):
        x, y = t
        return (sum(1 for (dx, dy) in ((-1, 0), (0, 1), (1, 0), (0, -1)) if self.getCell((x + dx, y + dy)) == '#')
                if 0 < x < self.rows - 1 and 0 < y < self.columns - 1 else None)

    def firstThreeWalls(self):
        for r, row in enumerate(self.data):
            for c, column in enumerate(row):
                if column == ' ' and self.numberWalls((r, c)) == 3:
                    return r, c
        return None

    def findRoute(self):
        while t := self.firstThreeWalls():
            self.setCell(t, '#')

    def invert(self):
        for r, row in enumerate(self.data):
            for c, column in enumerate(row):
                self.setCell((r, c), ' ' if self.getCell((r, c)) == '#' else '#')
        return self


s = """########### #
#     #   # #
# ### # # # #
#   #   # # #
### ##### # #
#   # ###   #
# ### # #####
# #   # #   #
# # # # ### #
# # # #     #
# # # # # ###
#   #   #   #
########### #"""
d = PerfectMaze(s)
d.findRoute()
print(d.invert())
