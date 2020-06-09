from itertools import chain
from re import split as rsplit


def split(string):
    return list(filter(None, rsplit("[^a-zA-Z]+", string)))


def sequence(words, start=0):
    seq = []
    while start < len(words):
        seq.append(words[start])
        start += len(words[start])
    return seq, start - len(words)


def kruskal(path, start=0, last=False):
    with open(path, "r") as file:
        lines = file.readlines()
        words = list(chain(*[split(line) for line in lines[:-1]]))
        last_line = split(lines[-1])

    seq, start = sequence(words, start=start)

    if last:
        assert start < len(last_line), "no word visited on last line"
        seq.append(last_line[start])
    else:
        seq += sequence(last_line, start=start)[0]
    return seq


def trick(path, last=False):
    with open(path, 'r') as file:
        wc = len(split(file.readline()))
    last_word = kruskal(path, last=last)[-1]
    for i in range(1, wc):
        if last_word != kruskal(path, i, last)[-1]:
            return False
    return True
