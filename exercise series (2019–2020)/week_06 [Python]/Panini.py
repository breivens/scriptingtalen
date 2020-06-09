from itertools import groupby


class Panini:
    def __init__(self, collection):
        if isinstance(collection, (list, set, tuple)):
            assert all(isinstance(item, int) for item in collection), "invalid stickers"
            self.collection = set(collection)
        else:
            assert isinstance(collection, int), "invalid stickers"
            self.collection = {collection}

    def __repr__(self):
        return ", ".join(Panini.grouper(self.collection))

    def __add__(self, other):
        return Panini(self.collection | other.collection)

    def __sub__(self, other):
        return Panini(self.collection - other.collection)

    @staticmethod
    def grouper(collection):
        for group in groupby(enumerate(sorted(collection)), lambda l: l[1] - l[0]):
            group = list(group[1])
            first, last = group[0][1], group[-1][1]
            yield str(first) if first == last else f"{first}-{last}"


print(Panini([1, 3, 4, 5, 6, 7, 9, 10, 11, 17, 19, 20]))
