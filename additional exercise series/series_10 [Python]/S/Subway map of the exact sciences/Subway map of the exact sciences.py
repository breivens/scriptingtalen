class Station:
    def __init__(self, name: str, year: str, description: str):
        self.name = name
        self.year = year
        self.description = description
        self.lines = dict()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, year={self.year!r}, description={self.description!r})"

    def __str__(self):
        return f"{self.name} ({self.year}, {self.description})"

    def __eq__(self, other):
        return (self.name, self.year, self.description) == (other.name, other.year, other.description)

    def link(self, key: str, value: object):
        assert key not in self.lines, f"station is already linked with line {key}"
        self.lines[key] = value

    def next(self, name: str):
        return self.lines.get(name)


class Metromap:
    def __init__(self, stations=None):
        self.lines = dict()
        self.stations = dict()
        if stations:
            self.addStations(stations)

    def beginstation(self, line: str):
        return self.lines[line][0] if line in self.lines else None

    def terminal(self, line: str):
        return self.lines[line][-1] if line in self.lines else None

    def expand(self, line: str, station: Station):
        if str(station) in self.stations:
            station = self.stations[str(station)]
        else:
            self.stations[str(station)] = station
        if line not in self.lines:
            self.lines[line] = [station]
        else:
            self.lines[line][-1].link(line, station)
            self.lines[line].append(station)

    def addStations(self, path: str):
        with open(path, 'r', encoding='utf-8') as f:
            from csv import reader
            stations = tuple(reader(f, delimiter='\t'))
        for line, name, year, description in stations:
            self.expand(line, Station(name, year, description))
