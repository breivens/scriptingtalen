def stressedWord(word: str, symbols: list) -> str:
    from re import search, sub, IGNORECASE
    stress = None
    prev_start = float('inf')
    for symbol in symbols:
        # search for substring
        symbol = search(symbol, word, flags=IGNORECASE)
        if symbol:
            # leftmost and longest
            if symbol.start() < prev_start or (symbol.start() == prev_start and len(symbol.group()) > len(stress)):
                stress = symbol.group()
                prev_start = symbol.start()
    if stress:
        word = sub(f'({stress})', r'[\1]', word, count=1, flags=IGNORECASE)
    return word


def stressedSentence(sentence: str, symbols=None) -> str:
    symbols = symbols or ['Ac', 'Ag', 'Al', 'Am', 'Ar', 'As', 'At', 'Au', 'B', 'Ba', 'Be', 'Bh',
                          'Bi', 'Bk', 'Br', 'C', 'Ca', 'Cd', 'Ce', 'Cf', 'Cl', 'Cm', 'Cn', 'Co',
                          'Cr', 'Cs', 'Cu', 'Db', 'Ds', 'Dy', 'Er', 'Es', 'Eu', 'F', 'Fe', 'Fl',
                          'Fm', 'Fr', 'Ga', 'Gd', 'Ge', 'H', 'He', 'Hf', 'Hg', 'Ho', 'Hs', 'I',
                          'In', 'Ir', 'K', 'Kr', 'La', 'Li', 'Lr', 'Lu', 'Lv', 'Md', 'Mg', 'Mn',
                          'Mo', 'Mt', 'N', 'Na', 'Nb', 'Nd', 'Ne', 'Ni', 'No', 'Np', 'O', 'Os',
                          'P', 'Pa', 'Pb', 'Pd', 'Pm', 'Po', 'Pr', 'Pt', 'Pu', 'Ra', 'Rb', 'Re',
                          'Rf', 'Rg', 'Rh', 'Rn', 'Ru', 'S', 'Sb', 'Sc', 'Se', 'Sg', 'Si', 'Sm',
                          'Sn', 'Sr', 'Ta', 'Tb', 'Tc', 'Te', 'Th', 'Ti', 'Tl', 'Tm', 'U', 'Uuo',
                          'Uup', 'Uus', 'Uut', 'V', 'W', 'Xe', 'Y', 'Yb', 'Zn', 'Zr']
    return ' '.join([stressedWord(word, symbols) for word in sentence.split()])


print(stressedSentence("Monty Python's Life of Brian."))
# "[Mo]nty [P]ython's [Li]fe [o]f [Br]ian."
print(stressedSentence("Monty Python's Life of Brian.", ['Th', 'T', 'hon', 'on']))
# "M[on]ty Py[th]on's Life of Brian."
