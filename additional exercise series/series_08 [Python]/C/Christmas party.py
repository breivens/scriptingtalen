def isValidDraw(draw: dict, composition: list or tuple or set, sameFamily=False):
    for k, v in draw.items():
        if k == v:
            return False
        if sameFamily:
            for family in composition:
                if {k, v} <= family:
                    return False
    return True


def makeDraw(composition: list or tuple or set):
    from random import sample
    family = set.union(*map(set, composition))
    members = len(family)
    return dict(zip(sample(family, members), sample(family, members)))


def makeValidDraw(composition: list or tuple or set, sameFamily=False):
    while not isValidDraw(draw := makeDraw(composition), composition, sameFamily):
        continue
    return draw
