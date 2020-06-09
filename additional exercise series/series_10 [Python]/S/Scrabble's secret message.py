from collections import Counter, defaultdict


class Bag:
    def __init__(self, string):
        self.content = dict(Counter(string))

    def __repr__(self):
        return f"{self.__class__.__name__}({''.join(sorted(k * v for k, v in self.content.items()))!r})"

    def __str__(self):
        groups = defaultdict(list)
        for letter, count in sorted(self.content.items()):
            groups[count].append(letter)
        return "\n".join(f"{k}: {''.join(v)}" for k, v in sorted(groups.items()))

    def remove(self, substring):
        to_remove = Counter(substring)
        assert all(letter in self.content and count <= self.content[letter]
                   for letter, count in to_remove.items()), "not all letters are in the bag"
        for letter, count in to_remove.items():
            self.content[letter] -= count
            if self.content[letter] == 0:
                del self.content[letter]


bag = Bag('IAMDIETINGIEATQUINCEJELLYLOTSOFGROUNDMAIZEGIVESVARIETYICOOKRHUBARBANDSODAWEEPANEWORPUTONEXTRAFLESH__')
bag.remove('AEERTYOXMCNB_S')
print(bag)
