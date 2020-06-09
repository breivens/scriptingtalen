def molecularFormula(compound: str) -> dict:
    from re import findall
    atoms = findall('[A-Z][a-z]*', compound)
    return {atom: atoms.count(atom) for atom in set(atoms)}


def isomers(compound1: str, compound2: str) -> bool:
    return molecularFormula(compound1) == molecularFormula(compound2)


structuralFormula1 = 'OCaOSeOO'
structuralFormula2 = 'HHCHHCHHCHHCHH'
structuralFormula3 = 'HHCHHHCCHHHCHH'

print(molecularFormula(structuralFormula1))
# {'Ca': 1, 'Se': 1, 'O': 4}
print(molecularFormula(structuralFormula2))
# {'H': 10, 'C': 4}
print(molecularFormula(structuralFormula3))
# {'C': 4, 'H': 10}

print(isomers(structuralFormula1, structuralFormula2))
# False
print(isomers(structuralFormula1, structuralFormula3))
# False
print(isomers(structuralFormula2, structuralFormula3))
# True
