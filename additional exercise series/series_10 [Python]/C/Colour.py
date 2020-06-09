class Colour:
    def __init__(self, r=0, g=0, b=0):
        self.r, self.g, self.b = map(lambda l: min(max(l, 0), 255), (r, g, b))

    def __repr__(self):
        return f"{self.r, self.g, self.b}"

    def inverse(self):
        return Colour(255 - self.r, 255 - self.g, 255 - self.b)

    def greyscale(self):
        gs = int(.3 * self.r + .59 * self.g + .11 * self.b)
        return Colour(gs, gs, gs)
