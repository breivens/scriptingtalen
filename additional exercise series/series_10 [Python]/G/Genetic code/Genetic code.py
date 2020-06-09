class GeneticCode:
    def __init__(self, path):
        from csv import reader
        with open(path, 'r', encoding='utf-8') as file:
            self.table = {k.upper(): v for k, v in reader(file, delimiter=' ')}

    def aminoacid(self, codon: str):
        new_codon = codon.upper().replace('U', 'T')
        assert len(codon) == 3 and set(new_codon) <= set('ACGT'), f"'{codon}' is not a valid codon."
        return self.table.get(new_codon)

    def protein(self, sequence: str):
        sequence = sequence.upper().replace('U', 'T')
        assert set(sequence) <= set('ACGT'), "invalid DNA or RNA sequence."
        return "".join(self.aminoacid("".join(codon)) for codon in zip(*[iter(sequence)] * 3))


code = GeneticCode('bacterial_code.txt')
print(code.table)
print(code.aminoacid('AAT'))
