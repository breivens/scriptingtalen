class Gene:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop

    def __len__(self):
        return abs(self.start - self.stop) + 1

    def __repr__(self):
        return f"{self.__class__.__name__}{self.start, self.stop}"

    def __str__(self):
        if self.start <= self.stop:
            return f"{self.start}..{self.stop}"
        return f"complement({self.stop}..{self.start})"

    def to_tuple(self):
        return min(self.start, self.stop), max(self.start, self.stop)


class Genome:
    def __init__(self, length: int):
        self.length = length
        self.genes = list()

    def __len__(self):
        return self.length

    def addGene(self, gene: Gene):
        assert gene.start >= 0 and gene.stop <= len(self), "invalid coordinate"
        self.genes.append(gene)

    def density(self, overlap=True):
        sequence = Genome.merge(self.genes) if overlap else self.genes
        return sum([len(gene) for gene in sequence]) / self.length * 100

    @staticmethod
    def merge(genes: list):
        sequence = list()
        gene = genes[0]
        for i in range(len(genes) - 1):
            start1, stop1 = gene.to_tuple()
            start2, stop2 = genes[i + 1].to_tuple()
            if start1 <= stop2 and start2 <= stop1:  # check if overlap
                gene = Gene(min(start1, start2), max(stop1, stop2))
            else:
                sequence.append(gene)
                gene = genes[i + 1]
        sequence.append(gene)
        return sequence
