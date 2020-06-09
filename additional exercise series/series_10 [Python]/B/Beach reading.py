from random import Random


class CharacterGenerator:
    def __init__(self, seed, alphabet='0123456789'):
        assert seed is not None, 'no seed was given'
        self.seed = seed
        self.alpha = alphabet
        self.generator = Random()
        self.generator.seed(self.seed)

    def __repr__(self):
        if self.alpha == '0123456789':
            return f'{self.__class__.__name__}({self.seed})'
        return f'{self.__class__.__name__}({self.seed}, alphabet={self.alpha!r})'

    def reset(self, seed):
        self.seed = seed
        self.generator = Random()
        self.generator.seed(self.seed)

    def sequence(self, length=1):
        return ''.join(self.generator.choice(self.alpha) for _ in range(length))
