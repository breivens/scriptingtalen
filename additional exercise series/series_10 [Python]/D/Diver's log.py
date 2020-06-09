class Dive:
    def __init__(self, initialpressure: float, ultimatepressure: float, starttime: str, endtime: str, depth: float):
        self.initialpressure, self.ultimatepressure = initialpressure, ultimatepressure
        self.starttime, self.endtime = starttime, endtime
        self.duration = self.determineDuration()
        self.depth = depth

    def determineDuration(self):
        h_st, m_st, h_et, m_et = map(int, self.starttime.split(':') + self.endtime.split(':'))
        return (60 * h_et + m_et) - (60 * h_st + m_st)

    def SACratio(self):
        return 33 * (self.initialpressure - self.ultimatepressure) / (self.duration * (self.depth + 33))


class Log:
    def __init__(self, *dive):
        self.dives = [*dive]

    def newDive(self, dive: Dive):
        self.dives.append(dive)

    def meanSACratio(self):
        return sum(dive.SACratio() for dive in self.dives) / len(self.dives)

    def meanSACratio2(self):  # less readable, but a tiny amount faster
        return sum(map(Dive.SACratio, self.dives)) / len(self.dives)


log = Log(Dive(3100, 1300, '11:52', '12:45', 35),
          Dive(2700, 1000, '11:16', '12:06', 40),
          Dive(2800, 1200, '11:26', '12:06', 60))

print(log.meanSACratio())
print(log.meanSACratio2())
log.newDive(Dive(2800, 1150, '11:54', '12:16', 95))
print(log.meanSACratio())
print(log.meanSACratio2())
