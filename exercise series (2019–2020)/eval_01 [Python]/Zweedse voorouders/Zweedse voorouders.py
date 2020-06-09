def familieleden(path):
    relaties = {}
    with open(path, 'r', encoding='utf-8') as file:
        for line in file.read().split('\n'):
            familieleden = line.split()
            if familieleden:
                for lid in familieleden:
                    if lid not in relaties:
                        relaties[lid] = {}
                moeder, vader, *kinderen = familieleden
                relaties[vader]['kinderen'] = relaties[moeder]['kinderen'] = set(kinderen)
                for kind in kinderen:
                    relaties[kind]['vader'] = vader
                    relaties[kind]['moeder'] = moeder
    return relaties


def voorouder(naam, zweeds, relaties):
    for voorouder in [zweeds[i:i + 3] for i in range(0, len(zweeds), 3)]:
        if voorouder == 'far':
            assert 'vader' in relaties[naam], 'onbekende voorouder'
            naam = relaties[naam]['vader']
        elif voorouder == 'mor':
            assert 'moeder' in relaties[naam], 'onbekende voorouder'
            naam = relaties[naam]['moeder']
    return naam


def nakomelingen(naam, generaties, relaties):
    generatie = {naam: ''}
    for _ in range(generaties):
        volgende_gen = {}
        for ouder, omschrijving in generatie.items():
            if 'kinderen' in relaties[ouder]:
                for kind in relaties[ouder]['kinderen']:
                    if 'vader' in relaties[kind] and relaties[kind]['vader'] == ouder:
                        volgende_gen[kind] = 'far' + omschrijving
                    else:
                        volgende_gen[kind] = 'mor' + omschrijving
        generatie = volgende_gen

    omschrijvingen = {}
    for naam, omschrijving in generatie.items():
        if omschrijving not in omschrijvingen:
            omschrijvingen[omschrijving] = set()
        omschrijvingen[omschrijving].add(naam)

    return omschrijvingen
