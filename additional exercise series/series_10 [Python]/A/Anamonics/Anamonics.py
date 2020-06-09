def anahook(root: str, anamonic: str) -> str or None:
    def count(container: iter):
        return {x: container.count(x) for x in set(container)}

    root, anamonic = root.lower(), anamonic.lower()

    for char in (a_count := count(anamonic)):
        if count(root + char) == a_count:
            return char
    return None


class Anamonic:
    def __init__(self, path: str):
        with open(path, 'r', encoding='utf-8') as f:
            self.words = [x for x in f.read().split('\n') if x]

    def anahooks(self, root: str) -> set:
        return {anahook(root, word) for word in self.words if anahook(root, word)}

    def isAnamonic(self, root: str, string: str) -> bool:
        return self.anahooks(root) == set(filter(str.isalpha, string.lower()))