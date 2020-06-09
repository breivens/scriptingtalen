def bundle(moons: dict) -> dict:
    planets = {}
    for moon, planet in moons.items():
        if planet not in planets:
            planets[planet] = set()
        planets[planet].add(moon)
    return planets


print(bundle({'Harpalyke': 'Jupiter', 'Psamathe': 'Neptune', 'Cordelia': 'Uranus', 'Cupid': 'Uranus'}))
# {'Neptune': {'Psamathe'}, 'Jupiter': {'Harpalyke'}, 'Uranus': {'Cordelia', 'Cupid'}}
print(bundle({'Farbauti': 'Saturn', 'Ananke': 'Jupiter', 'Sinope': 'Jupiter', 'Kalyke': 'Jupiter'}))
# {'Jupiter': {'Ananke', 'Sinope', 'Kalyke'}, 'Saturn': {'Farbauti'}}
print(bundle({'Callisto': 'Jupiter', 'Adrastea': 'Jupiter', 'Helene': 'Saturn'}))
# {'Jupiter': {'Callisto', 'Adrastea'}, 'Saturn': {'Helene'}}
