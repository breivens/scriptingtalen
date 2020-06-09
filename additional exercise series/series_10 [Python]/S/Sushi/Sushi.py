class Ingredient:
    def __init__(self, japanese: str, english=None):
        self._japanese = japanese
        self._english = english or japanese

    def __str__(self):
        return self.japanese()

    def japanese(self):
        return self._japanese

    def english(self):
        return self._english


class Sushi:
    description = '{ingredients}'
    rice = Ingredient('su-meshi', 'sushi rice')
    seaweed = Ingredient('nori', 'seaweed')

    def __init__(self, ingredients: list):
        self.ingredients = ingredients

    def __str__(self):
        ingredients = Sushi.summarize(tuple(map(str, self.ingredients)))
        return self.description.format(rice=str(self.rice), seaweed=str(self.seaweed), ingredients=ingredients)

    def english(self):
        ingredients = Sushi.summarize(tuple(map(Ingredient.english, self.ingredients)))
        return self.description.format(rice=self.rice.english(), seaweed=self.seaweed.english(),
                                       ingredients=ingredients)

    @staticmethod
    def summarize(ingredients: tuple):
        if len(ingredients) < 3:
            return " and ".join(ingredients)
        return ", ".join(ingredients[:-1]) + f" and {ingredients[-1]}"


class Maki(Sushi):
    description = '{ingredients} rolled in {rice} and {seaweed}'


class Futomaki(Maki):
    description = '{ingredients} rolled in {rice} and {seaweed}, with {seaweed} facing out'


class Temaki(Maki):
    description = 'cone of {seaweed} filled with {rice} and {ingredients}'


class Uramaki(Maki):
    description = '{ingredients} rolled in {seaweed} and {rice}, with {rice} facing out'


class InvalidSushiError(Exception):
    pass


class Nigiri(Sushi):
    description = 'hand-formed {rice} topped with {ingredients}'

    def __init__(self, ingredients):
        if len(ingredients) != 1:
            raise InvalidSushiError('Nigiri has only one topping')
        Sushi.__init__(self, ingredients)


class Gunkanmaki(Nigiri):
    description = '{ingredients} on {rice} wrapped in a strip of {seaweed}'


class Temarizushi(Nigiri):
    description = '{ingredients} pressed into a ball of {rice}'


class SushiMaker:
    sushi_types = {'sushi': Sushi, 'maki': Maki, 'futomaki': Futomaki, 'temaki': Temaki, 'uramaki': Uramaki,
                  'nigiri': Nigiri, 'gunkanmaki': Gunkanmaki, 'temarizushi': Temarizushi}

    def __init__(self, file=None):
        if not file:
            file = open('sushi.txt', 'r', encoding='utf-8')
        self.ingredientIndex = self.indexIngredients(file.read())

    @staticmethod
    def indexIngredients(ingredients: str):
        translations = [i.split("\t") for i in ingredients.split('\n') if not i.startswith('#')]
        return {t[0]: Ingredient(*t if len(t) == 2 else t) for t in translations}

    def makeSushi(self, ingredients: str):
        ingredients = [self.ingredientIndex.get(ingredient, ingredient) for ingredient in ingredients.split()]
        if ingredients[-1] in self.sushi_types:
            sushi_type = self.sushi_types[ingredients[-1]]
            return sushi_type(ingredients[:-1])
        return Sushi(ingredients)
