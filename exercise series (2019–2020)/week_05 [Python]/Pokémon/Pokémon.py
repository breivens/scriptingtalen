def damage(path):
    relationships = {}
    for line in open(path, 'r'):
        type1, type2, factor = line.split()
        if type1 not in relationships:
            relationships[type1] = {}
        relationships[type1][type2] = float(factor)
    return relationships


def effectiveness(attack, defenders, file):
    relationships = damage(file)
    factor = 1.0
    for defender in defenders.split():
        factor *= relationships[attack].get(defender, 1.0)
    return factor
