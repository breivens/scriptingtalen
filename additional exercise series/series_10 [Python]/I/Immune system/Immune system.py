class Organism:
    def __init__(self, path=None):
        self.innate = list()
        self.adaptive = list()
        if path:
            with open(path, 'r', encoding='utf-8') as file:
                self.innate = list(map(int, filter(None, (file.read().split('\n')))))

    def isResistant(self, virus: int):
        if virus in self.innate:
            return True
        self.adaptive.append(virus)
        return self.adaptive.count(virus) >= 3

    def mutation(self, virus: int):
        self.innate = list(filter(virus.__ne__, self.innate))
        self.adaptive = list(filter(virus.__ne__, self.adaptive))
