class Diana:
    def __init__(self, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        self.pads = "".join(filter(str.isalpha, content)).upper()

    def index(self, prefix: str):
        prefix = "".join(filter(str.isalpha, prefix.upper()))
        assert prefix in self.pads, "invalid prefix"
        return self.pads.index(prefix) + len(prefix)

    @staticmethod
    def trigraph(char1: str, char2: str):
        return chr((155 - ord(char1.upper()) - ord(char2.upper())) % 26 + 65)

    def encode(self, string: str, n=10):
        string = "".join(filter(str.isalpha, string)).upper()
        prefix, message = string[:n], string[n:]
        i = self.index(prefix)
        assert i + len(message) < len(self.pads), "one-time pad is too short.txt"
        return "".join(Diana.trigraph(char1, char2) for char1, char2 in zip(message, self.pads[i:i + len(message)]))

    def decode(self, string: str, n=10):
        return self.encode(string, n)


diana = Diana("otp.txt")
print(diana.encode('CMMXT VYTJI RRQGU meet at ten tonight', 15))
