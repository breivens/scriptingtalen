class Census:
    def __init__(self, year: int, path: str):
        from csv import reader
        with open(path, 'r', encoding='utf-8') as file:
            censuses = {row[0]: row[1:] for row in list(reader(file))}

        assert str(year) in censuses.get('REGION', ''), "no data available"

        year_index = censuses.pop('REGION').index(str(year))
        self.population = {r: int(c[year_index]) for r, c in censuses.items()}  # population in <year>

    def citizens(self, region: str):
        assert region in self.population, "no data available"
        return self.population[region]

    def allocation(self, n: int):
        from math import sqrt
        assert len(self.population) <= n, "too few representatives"

        rcount = dict.fromkeys(self.population, 1)
        for _ in range(n - len(rcount)):
            region = max(self.population, key=lambda r: self.population[r] / sqrt(rcount[r] * (rcount[r] + 1)))
            rcount[region] += 1
        return rcount


us2010 = Census(2010, 'us_population.csv')
print(us2010.population)
print(us2010.citizens('Alabama'))
print(us2010.allocation(435))