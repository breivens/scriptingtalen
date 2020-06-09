class proteinDB:
    def __init__(self):
        self.peptides = dict()

    @staticmethod
    def isPeptide(peptide: str):
        s, k, r = peptide[-1], peptide.count('K'), peptide.count('R')
        return 5 <= len(peptide) <= 50 and ((s, k, r) == ('K', 1, 0) or (s, k, r) == ('R', 0, 1))

    def addPeptide(self, label: str, peptide: str):
        assert proteinDB.isPeptide(peptide), "invalid peptide"
        if peptide not in self.peptides:
            self.peptides[peptide] = set()
        self.peptides[peptide].add(label)

    def addProtein(self, label: str, protein: str):
        def index(char: str, sequence: str):
            return sequence.index(char) if char in sequence else float('inf')

        while protein:
            peptide, peptide_end, protein = protein.partition('K' if index('K', protein) < index('R', protein) else 'R')
            peptide += peptide_end
            if proteinDB.isPeptide(peptide):
                self.addPeptide(label, peptide)

    def addProteins(self, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                label, protein = line.split()
                self.addProtein(label, protein)

    def identify(self, peptides: list or tuple or set):
        labels = [self.peptides[peptide] for peptide in peptides if peptide in self.peptides]
        return sorted(set.intersection(*labels)) if labels else list()


unipept = proteinDB()
unipept.addProteins('proteins.txt')
print(unipept.peptides)

