from collections import deque


class Cryptex:
    def __init__(self, path, combinatie=None):
        with open(path, "r", encoding='utf-8') as f:
            content = f.read()
        self.disks = list(filter(None, content.split('\n')))
        assert self.disks, "ongeldige schijven"  # not a edge case on dodona
        self.rings = list(map("".join, zip(*self.disks)))
        self.key = combinatie or self.rings[0]
        self.instellen(self.key)

        assert all(
            len(next(iter(self.disks))) == len(disk) == len(set(disk)) for disk in self.disks), "ongeldige schijven"

    def __str__(self):
        return "\n".join(map(" ".join, self.rings))

    def ring(self, index):
        return self.rings[index]

    def ontgrendeld(self):
        return self.ring(0) == self.key

    def instellen(self, new_key):
        assert all(new_key[i] in self.disks[i] for i in range(len(new_key))), "ongeldige combinatie"
        self.key = new_key

    def roteer(self, rotations):
        for disk, count in rotations.items():
            r_disk = deque(self.disks[disk])
            r_disk.rotate(-count)
            self.disks[disk] = "".join(r_disk)
        self.rings = list(map("".join, zip(*self.disks)))


c = Cryptex('cryptex.txt')
print(f"key: '{c.key}'\nunlocked: {c.ontgrendeld()}\ncryptex:\n{c}\n")
c.instellen('HOUSE')
print(f"key: '{c.key}'\nunlocked: {c.ontgrendeld()}\ncryptex:\n{c}\n")
c.roteer({0: 4, 1: 5, 2: 9, 3: 8, 4: 2})
print(f"key: '{c.key}'\nunlocked: {c.ontgrendeld()}\ncryptex:\n{c}")

# ALL POSSIBLE CONFIGURATIONS FOR THE CRYPTEX:
# self.config = list(map("".join, itertools.product(*self.disks)))
# THE CORRESPONDING ASSERTION:
# assert new_key in self.combinations, "invalid combination"
