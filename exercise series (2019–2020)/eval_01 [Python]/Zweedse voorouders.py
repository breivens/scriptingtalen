def familieleden(path):
    relaties = {}
    with open(path, 'r', encoding='utf-8') as file:
        while line := file.readline():
            line = line.strip()
            if line:
                line = line.split()
                moeder, vader, kinderen = line[0], line[1], line[2:]
                if vader in relaties:
                    relaties[vader].update({'kinderen': set(kinderen)})
                else:
                    relaties[vader] = {'kinderen': set(kinderen)}
                if moeder in relaties:
                    relaties[moeder].update({'kinderen': set(kinderen)})
                else:
                    relaties[moeder] = {'kinderen': set(kinderen)}
                for kind in kinderen:
                    if kind in relaties:
                        relaties[kind].update({'moeder': moeder, 'vader': vader})
                    else:
                        relaties[kind] = {'moeder': moeder, 'vader': vader}
    return relaties


def voorouder(naam, zweeds, relaties):
    while zweeds:
        assert 'vader' in relaties[naam] and 'moeder' in relaties[naam], "onbekende voorouder"
        if zweeds[:3] == 'far':
            naam = relaties[naam]['vader']
        elif zweeds[:3] == 'mor':
            naam = relaties[naam]['moeder']
        zweeds = zweeds[3:]
    return naam


def nakomelingen(naam, getal, relaties):
    generaties = {}
    namen = [naam]
    for i in range(getal):
        for naam in namen:
            namen = namen.remove(naam)
            for kind in tuple(*relaties[naam].values()):
                print(kind)
                namen.append(kind)
    return generaties


relaties = familieleden("data.txt")
print(nakomelingen('Ronan', 1, relaties))
