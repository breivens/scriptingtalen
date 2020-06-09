class Cowsay:
    def __init__(self, sequence):
        self.message = sequence
        self.eyes = 'o', 'o'
        self.path = 'cow.cow'

    def __repr__(self):
        line = ['+' + '-' * (m := len(max(self.message, key=len)) + 2) + '+']
        return "\n".join(line + list(map(lambda l: "|" + l.center(m) + "|", self.message)) + line)

    def __str__(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            content = file.read()
        return self.__repr__() + "\n" + content.strip("\n").replace("{}", self.eyes[0], 1).replace("{}", self.eyes[1])

    def setEyes(self, eyes):
        assert isinstance(eyes, str) and len(eyes) == 2, "invalid eyes"
        self.eyes = tuple(eyes)

    def setImage(self, path):
        self.path = path


quote = Cowsay(['Moo may represent an idea,', 'but only the cow knows.'])
quote.setEyes('$$')
print(quote)
