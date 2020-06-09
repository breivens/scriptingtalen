# noinspection Duplicates
class Doolhof:
    buren = ((0, -1), (-1, 0), (0, 1), (1, 0))

    def __init__(self, bestandsnaam):
        # rooster opbouwen op basis van bestandsinhoud
        self.rooster, self.ingang, self.uitgang = [], None, None
        for r, regel in enumerate(open(bestandsnaam, 'r')):
            rij = []
            for c, cel in enumerate(regel.rstrip('\n')):
                if cel == ' ':
                    rij.append(0.0)
                elif cel == '#':
                    rij.append(-1.0)
                elif cel == '+':
                    rij.append(1.0)
                    assert self.ingang is None, 'meerdere ingangen'
                    self.ingang = (r, c)
                else:
                    rij.append(0.0)
                    assert self.uitgang is None, 'meerdere uitgangen'
                    self.uitgang = (r, c)
            self.rooster.append(rij)
        assert self.ingang, 'geen ingang'
        assert self.uitgang, 'geen uitgang'
        # bepaal aantal rijen en kolommen van het rooster
        self.rijen = len(self.rooster)
        self.kolommen = len(self.rooster[0])

    def __repr__(self):
        decimalen = 3
        breedte = 2 + decimalen
        return '\n'.join(
            ' '.join(('#' * breedte) if cel < 0 else f'{cel:.{decimalen}f}' for cel in rij) for rij in self.rooster)

    def __str__(self):
        route = set(self.route())

        def weergave(r, c, cel):
            if (r, c) == self.ingang:
                return '+'
            elif (r, c) == self.uitgang:
                return '-'
            elif cel < 0:
                return '#'
            else:
                return ' ~'[(r, c) in route]

        return '\n'.join(
            ''.join(weergave(r, c, cel) for c, cel in enumerate(rij)) for r, rij in enumerate(self.rooster))

    def isvloeibaar(self, r, c):
        return 0 <= r < self.rijen and 0 <= c < self.kolommen and self.rooster[r][c] >= 0

    def volgende_niveau(self, positie, debiet):
        r, c = positie
        # vloeistofniveau verandert nooit bij ingang, uitgang en muur
        if (r, c) in {self.ingang, self.uitgang} or not self.isvloeibaar(r, c):
            return self.rooster[r][c]
        # huidige vloeistofniveau opzoeken
        huidige_niveau = self.rooster[r][c]
        # vloeistofniveau bijwerken op basis van vloeistofniveau bij buren
        return huidige_niveau + sum(
            debiet * (self.rooster[r + dr][c + dc] - huidige_niveau) for (dr, dc) in self.buren if
            self.isvloeibaar(r + dr, c + dc))

    def simuleer_niveau(self, debiet, stappen=1):
        for _ in range(stappen):
            # vloeistofniveau bijwerken in alle cellen van het rooster
            # OPMERKING: nieuw rooster opbouwen in plaats van bestaande rooster
            # te overschrijven, omdat buurcellen elkaar beïnvloeden
            self.rooster = [[self.volgende_niveau((r, c), debiet) for c in range(self.kolommen)] for r in
                            range(self.rijen)]
        return self

    def route(self):
        r, c = self.ingang
        huidige_niveau = self.rooster[r][c]
        vorige_niveau = 1.0 + huidige_niveau
        route = []
        while huidige_niveau < vorige_niveau:
            # huidige cel aan route toevoegen
            route.append((r, c))
            # volgende cel op de route zoeken
            vorige_niveau = huidige_niveau
            huidige_niveau, r, c = min((self.rooster[r + dr][c + dc], r + dr, c + dc) for dr, dc in self.buren if
                                       self.isvloeibaar(r + dr, c + dc))
        return route
