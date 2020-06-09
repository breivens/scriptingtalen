class Compass:
    dirs = ("north", "east", "east", "south", "south", "west", "west", "north")

    def __init__(self, angle=0):
        self.angle = angle % 360
        self.dir = Compass.dirs[self.angle // 45]

    def __repr__(self):
        return f"{self.__class__.__name__}({self.angle})"

    def __str__(self):
        return f"{self.angle}° ({self.dir})"

    def turn(self, angle):
        self.angle = (self.angle + angle) % 360
        self.dir = Compass.dirs[self.angle // 45]

    def direction(self):
        return self.dir
