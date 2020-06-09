def addCountryProperty(property: str, values: dict, properties=None):
    dictionary = properties or {}
    for country, value in values.items():
        if country not in dictionary:
            dictionary[country] = {}
        dictionary[country].update({property: value})
    return dictionary


capitals = {'Belgium': 'Brussels',
            'Netherlands': 'Amsterdam',
            'France': 'Paris',
            'Germany': 'Berlin'}

population = {'Belgium': 10438353,
              'Netherlands': 16730632,
              'France': 62814233,
              'Germany': 81305856}

properties = addCountryProperty('capital', capitals)
print(addCountryProperty('population', population, properties))
