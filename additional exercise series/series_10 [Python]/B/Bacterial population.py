class Population:
    def __init__(self, m=0, n=0, k=0):
        self.population = [*[1] * m, *[2] * n, *[3] * k]
        self.m, self.n, self.k = m, n, k
        self.encounters = 0

    def __str__(self):
        return f'type I: {self.m}, type II: {self.n}, type III: {self.k} (after {self.encounters} encounters)'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.m}, {self.n}, {self.k})'

    def plasmids(self) -> tuple:
        return self.m, self.n, self.k

    def size(self) -> int:
        return self.m + self.n + self.k

    def encounter(self, i: int, j: int):
        self.encounters += 1
        bacteria = {self.population[i], self.population[j]}
        if len(bacteria) == 2:
            if bacteria == {1, 2}:
                self.population[i], self.population[j] = 3, 3
                self.m -= 1
                self.n -= 1
                self.k += 2
            elif bacteria == {1, 3}:
                self.population[i], self.population[j] = 2, 2
                self.m -= 1
                self.n += 2
                self.k -= 1
            elif bacteria == {2, 3}:
                self.population[i], self.population[j] = 1, 1
                self.m += 2
                self.n -= 1
                self.k -= 1


def simulation(population: Population, number=1, display=1):
    from random import sample
    for _ in range(number):
        if population.encounters % display == 0:
            print(population)
        population.encounter(*sample(range(population.size()), k=2))
    print(population)


simulation(a := Population(m=998, n=1, k=1), 10000, 2500)
# With a correct implementation of the class Population you should see that after some time, the three
# types of plasmids are about equally divided over the population.
