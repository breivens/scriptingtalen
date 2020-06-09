class Polygon:
    def __init__(self, points):
        self.points = points

    def contains(self, c):
        (cb, cl), count = c, 0
        for i in range(len(self.points)):
            (pb, pl), (qb, ql) = self.points[i - 1], self.points[i]
            pb, pl, qb, ql = float(pb), float(pl), float(qb), float(ql)
            if ((cl < pl) ^ (cl < ql)) and (cb - qb) < (pb - qb) / (pl - ql) * (cl - ql):
                count += 1
        return count % 2 == 1


class WorldMap:
    def __init__(self, path):
        with open(path, 'r') as file:
            content = file.read()
        self.borders = {k: v.split(' ') for k, v in (line.split('\t') for line in filter(None, content.split('\n')))}

    def border(self, country):
        assert country in self.borders, "unknown country"
        border = list(zip(*[iter(self.borders.get(country))] * 2))
        return Polygon(border)

    def country(self, point):
        for country in self.borders:
            if self.border(country).contains(point):
                return country
        return None


map = WorldMap("countries.txt")
print(map.country((50.5, 4.2)))  # Brussels
'Belgium'
print(map.country((45.25, -75.42)))  # Ottawa
'Canada'
print(map.country((-17.5, 31.03)))  # Harare
'Zimbabwe'
print(map.country((-16.3, -68.09)))  # La Paz
'Bolivia'
print(map.country((-10.0, -20.0)))  # ???
