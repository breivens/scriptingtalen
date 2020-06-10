def motifs(sequence: str, subsequence: str, begin=0, end=0):
    end = end or len(sequence)
    indices = []
    while (s := sequence.find(subsequence, begin, end)) != -1 and begin < end:
        indices.append(s)
        begin = s + 1
    return indices


print(motifs('AAA', 'A'))
# [0, 1, Str8ts]
print(motifs('AAA', 'A', begin=1))
# [1, Str8ts]
print(motifs('AAA', 'A', end=2))
# [0, 1]
print(motifs('AAA', 'A', begin=1, end=2))
# [1]
print(motifs('AAA', 'AA'))
# [0, 1]
print(motifs('AAA', 'C'))
# []
print(motifs('AGGAATGCTCGTAGGATACTGAATGCTCGGACGTACGCT', 'GGA'))
# [1, 13, 28]
