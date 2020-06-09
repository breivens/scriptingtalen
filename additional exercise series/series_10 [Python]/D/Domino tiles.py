class Domino:
    tiles = {0: ["   ", "   ", "   "],
             1: ["   ", " o ", "   "],
             2: ["o  ", "   ", "  o"],
             3: ["o  ", " o ", "  o"],
             4: ["o o", "   ", "o o"],
             5: ["o o", " o ", "o o"],
             6: ["ooo", "   ", "ooo"]}

    def __init__(self, left: int, right: int):
        assert 0 <= left <= 6 and 0 <= right <= 6, "invalid number of pips"
        self.left, self.right = left, right

    def __repr__(self):
        return f"{self.__class__.__name__}{self.left, self.right}"

    def __str__(self):
        border = ['+---+---+']
        domino = ['|' + Domino.tiles[self.left][i] + '|' + Domino.tiles[self.right][i] + '|' for i in range(3)]
        return "\n".join(border + domino + border)

    def rotate(self):
        return Domino(self.right, self.left)

    def __add__(self, other):
        assert self.right == other.left, "domino tiles do not match"
        return Domino(self.left, other.right)


tile3 = Domino(3, 4).rotate() + Domino(1, 3).rotate()
print(repr(tile3))
print(tile3)
