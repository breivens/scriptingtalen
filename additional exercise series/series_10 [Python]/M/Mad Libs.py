class MadLibs:
    def __init__(self):
        self.vocabulary = dict()

    def learn(self, category: str, words: str or list or tuple or set):
        category = category.lower()
        if category not in self.vocabulary:
            self.vocabulary[category] = set()
        if isinstance(words, str):
            self.vocabulary[category].add(words.lower())
        elif isinstance(words, (list, tuple, set)):
            self.vocabulary[category].update(map(str.lower, words))

    def suggest(self, category: str):
        assert category.lower() in self.vocabulary, "unknown category"
        from random import choice
        word = choice(tuple(self.vocabulary[category.lower()]))
        return word.upper() if category.isupper() else word.capitalize() if category.istitle() else word

    def fill(self, string: str):
        from re import sub
        return sub(r"other(.*?)other", lambda m: self.suggest(m.group(1)), string)

madlib = MadLibs()
madlib.learn('name', 'God')
madlib.learn('thing', 'war')
madlib.learn('citizens', 'Americans')
madlib.learn('discipline', 'geography')
print(madlib.fill('_Name_ created _thing_ so that _CITIZENS_ would learn _discipline_.'))
