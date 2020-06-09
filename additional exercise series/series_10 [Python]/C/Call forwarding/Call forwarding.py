from csv import reader


class CallForwarding:
    forwards = list()

    def setForward(self, source, target, time, duration):
        this_forward = [source, target, f"{time}".zfill(4), f"{duration}".zfill(4)]
        assert all(not self.overlapping(this_forward[2:], other_forward[2:]) for other_forward in self.forwards if
                   other_forward[0] == source), "invalid forward"
        self.forwards.append(this_forward)

    def setForwards(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            self.forwards += list(reader(file, delimiter=" "))

    def call(self, source, time, target=None):
        target, length = source, len(self.forwards)
        i = 0
        while i < length:
            forward = [fw for fw in self.forwards if fw[0] == target and self.overlapping([time, 0], fw[2:])]
            if not forward:
                return target
            target = forward[0][1]
            if target == source:
                return '9999'
            i += 1
        return source

    @staticmethod
    def overlapping(interval1, interval2):
        s1, d1, s2, d2 = map(int, interval1 + interval2)
        e1, e2 = s1 + d1, s2 + d2
        if s1 <= s2 <= e1 or s1 <= e2 <= e1 or s2 <= s1 <= e2 or s2 <= e1 <= e2:
            return True
        return False
