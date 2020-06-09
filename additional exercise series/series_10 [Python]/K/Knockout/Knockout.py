from math import log


def letter_frequencies(string: str):
    from collections import Counter
    return dict(Counter(filter(str.isalpha, string.upper())))


class Knockout:
    def __init__(self, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            from csv import reader
            self.capitals = {line[0].upper(): line[1] for line in reader(file)}

    def capital(self, country: str):
        country = country.upper()
        assert country in self.capitals, "unknown country"
        return self.capitals[country]

    def ordinary_time(self, home: str, away: str):
        hc, ac = self.capital(home).upper(), self.capital(away).upper()
        h_freq, hc_freq, a_freq, ac_freq = (
            letter_frequencies(home), letter_frequencies(hc), letter_frequencies(away), letter_frequencies(ac))
        return (sum(min(h_freq[char], ac_freq[char]) for char in filter(str.isalpha, set(home.upper()) & set(ac))),
                sum(min(a_freq[char], hc_freq[char]) for char in filter(str.isalpha, set(away.upper()) & set(hc))))

    def extra_time(self, home: str, away: str):
        hc, ac = self.capital(home).upper(), self.capital(away).upper()
        h_freq, hc_freq, a_freq, ac_freq = (
            letter_frequencies(home), letter_frequencies(hc), letter_frequencies(away), letter_frequencies(ac))
        return (sum(h_freq[char] * ac_freq[char] for char in filter(str.isalpha, set(home.upper()) & set(ac))),
                sum(a_freq[char] * hc_freq[char] for char in filter(str.isalpha, set(away.upper()) & set(hc))))

    def match(self, home: str, away: str):
        h, a = self.ordinary_time(home, away)
        if h != a:
            return home if h > a else away
        h, a = self.extra_time(home, away)
        if h != a:
            return home if h > a else away
        return home if home.upper() < away.upper() else away

    def winner(self, countries: list or tuple):
        for _ in range(int(log(len(countries), 2))):
            countries = list(zip(*[iter(countries)] * 2))
            for i, (home, away) in enumerate(countries):
                countries[i] = self.match(home, away)
        return countries[0]
