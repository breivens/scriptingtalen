class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __repr__(self):
        return f'{self.__class__.__name__}{self.x, self.y!r}'

    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    def __le__(self, other):
        if self.x == other.x:
            return self.y <= other.y
        return self.x <= other.x

    def __gt__(self, other):
        if self.x == other.x:
            return self.y > other.y
        return self.x > other.x

    def __ge__(self, other):
        if self.x == other.x:
            return self.y >= other.y
        return self.x >= other.x

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        return (self.x, self.y) != (other.x, other.y)

    def distance(self, other):
        from math import sqrt
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Linesegment:
    def __init__(self, point1: Point, point2: Point):
        assert point1 != point2, 'line segment must have length greater than zero'
        self.point1, self.point2 = min(point1, point2), max(point1, point2)  # left and right

    def __repr__(self):
        return f'{self.__class__.__name__}{self.point1, self.point2!r}'

    def length(self):
        return self.point1.distance(self.point2)


class Rectangle:
    def __init__(self, point1: Point, point2: Point):
        assert point1 != point2, 'rectangle must have area greater than zero'
        min_x, min_y = min(point1.x, point2.x), min(point1.y, point2.y)  # bottom left
        max_x, max_y = max(point1.x, point2.x), max(point1.y, point2.y)  # top right
        self.point1, self.point2 = Point(min_x, min_y), Point(max_x, max_y)

    def __repr__(self):
        return f'{self.__class__.__name__}{self.point1, self.point2!r}'

    def area(self):
        return abs((self.point1.x - self.point2.x) * (self.point1.y - self.point2.y))

    def intersects(self, other):
        return not (self.point2.x < other.point1.x
                    or self.point1.x > other.point2.x
                    or self.point2.y < other.point1.y
                    or self.point1.y > other.point2.y)

    def intersection(self, other):
        if self.intersects(other):
            # bottom left of intersection
            x1 = max(min(self.point1.x, self.point2.x), min(other.point1.x, other.point2.x))
            y1 = max(min(self.point1.y, self.point2.y), min(other.point1.y, other.point2.y))
            # top right of intersection
            x2 = min(max(self.point1.x, self.point2.x), max(other.point1.x, other.point2.x))
            y2 = min(max(self.point1.y, self.point2.y), max(other.point1.y, other.point2.y))
            # intersection = point
            if x1 == x2 and y1 == y2:
                return Point(x1, y1)
            # intersection = line
            if x1 == x2 or y1 == y2:
                return Linesegment(Point(x1, y1), Point(x2, y2))
            # intersection = rectangle
            return Rectangle(Point(x1, y1), Point(x2, y2))
        return None
