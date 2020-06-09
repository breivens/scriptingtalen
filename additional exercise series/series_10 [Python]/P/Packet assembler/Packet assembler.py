class Assembler:
    def __init__(self, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            self.packets = [packet + [''] * (len(packet) == 3) for packet in
                            [line.strip().split('\t') for line in file]]

    def count(self, m: int):
        return sum(1 for packet in self.packets if int(packet[0]) == m)

    def isComplete(self, m: int):
        for packet in self.packets:
            if int(packet[0]) == m:
                return self.count(m) == int(packet[2])
        return False

    def completeMessages(self):
        return {int(packet[0]) for packet in self.packets if self.isComplete(int(packet[0]))}

    def incompleteMessages(self):
        return {int(packet[0]): (self.count(int(packet[0])), int(packet[2]))
                for packet in self.packets if not self.isComplete(int(packet[0]))}

    def message(self, m: int):
        assert self.isComplete(m), "incomplete message"
        return "\n".join([f"{i}. {message}" for i, message in
                          sorted([(int(packet[1]), packet[3]) for packet in self.packets if int(packet[0]) == m])])


assembler = Assembler('packets_02.txt')
print(assembler.message(2997))
