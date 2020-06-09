def profile(sequence: list or tuple) -> dict:
    assert len(set(map(len, sequence))) == 1, 'sequences should have equal length'
    counter = {'A': [], 'C': [], 'G': [], 'T': []}
    for row in zip(*sequence):
        counter['A'].append(row.count('A'))
        counter['C'].append(row.count('C'))
        counter['G'].append(row.count('G'))
        counter['T'].append(row.count('T'))
    return counter


def consensus1(profile: dict) -> str:
    sequence = ''
    base = ''.join(profile.keys())
    for column in zip(*profile.values()):
        base_count = max(column)
        sequence += 'N' if column.count(base_count) > 1 else base[column.index(base_count)]
    return sequence


def consensus2(profile: dict) -> str:
    sequence = ''
    for i in range(len(profile['A'])):
        char = count = 0
        for base in 'ACGT':
            base_count = profile[base][i]
            if count < base_count:
                char, count = base, base_count
            elif count == base_count:
                char = 'N'
        sequence += char
    return sequence


seqs = ['GCAAAACG', 'GCGAAACT', 'TACCTTCA', 'TATGTTCA', 'GCCTTAGG', 'GACTTATA', 'TCGGATCC']
print(consensus1(profile(seqs)))
print(consensus2(profile(seqs)))
