from csv import reader


class CountryMap:
    def __init__(self, path1, path2):
        with open(path1, 'r', encoding='utf-8') as file1:
            self.countries = dict(reader(file1, delimiter='\t'))
        with open(path2, 'r', encoding='utf-8') as file2:
            self.n_countries = list(reader(file2, delimiter='\t'))

    def numberCountries(self):
        return len(self.countries.keys())

    def numberColours(self):
        return len(set(self.countries.values()))

    def colour(self, country):
        assert country in self.countries, "unknown country"
        return self.countries[country]

    def neighbours(self, country):
        assert country in self.countries, "unknown country"
        return set(map(lambda l: l[1], filter(lambda l: l[0] == country, self.n_countries)))

    def areNeighbours(self, country1, country2):
        assert country1 and country2 in self.countries, "unknown country"
        return country2 in self.neighbours(country1)

    def invalidNeighbours(self):
        invalids = []
        for country1, colour in self.countries.items():
            for country2 in self.neighbours(country1):
                if colour == self.colour(country2):
                    country1, country2 = sorted((country1, country2))
                    invalids.append((country1, country2, colour))
        return sorted(invalids)