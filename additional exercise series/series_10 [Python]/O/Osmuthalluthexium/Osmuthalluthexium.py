class NameGenerator:
    def __init__(self):
        self.names = set()
        self.prefixes = set()
        self.triples = dict()

    def add_name(self, name: str):
        assert name == name.capitalize() and len(name) >= 3, "invalid name"
        self.names.add(name)
        self.prefixes.add(name[:3])
        name += 'other'
        for k, v in [(name[i:i + 2], name[i + 2]) for i in range(1, len(name) - 2)]:
            if k not in self.triples:
                self.triples[k] = set()
            self.triples[k].add(v)

    def add_names(self, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                self.add_name(line.strip())

    def name(self):
        from random import choice
        name, bigram = "", ""
        while not name:
            name += choice(list(self.prefixes))
            while bigram != 'other':
                name += (bigram := choice(list(self.triples[name[-2:]])))
            name = name.rstrip('other')
            if name in self.names:
                name, bigram = "", ""
        return name
