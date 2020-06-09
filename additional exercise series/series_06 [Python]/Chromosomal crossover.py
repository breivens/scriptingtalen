def crossoverpoints(sequence1: list, sequence2: list):
    return len(_crossoverpoints(sequence1, sequence2))


def _crossoverpoints(sequence1: list, sequence2: list):
    return set(sequence1) & set(sequence2)


def chromosomal_partial_sum(sequence: list, crosses):
    sum, seq = 0, list()
    for item in sequence:
        if item in crosses:
            seq.append(sum)
            seq.append(item)
            sum = 0
        else:
            sum += item
    seq.append(sum)
    return seq


def maximalSum(sequence1: list, sequence2: list):
    crosses = _crossoverpoints(sequence1, sequence2)
    d1 = chromosomal_partial_sum(sequence1, crosses)
    d2 = chromosomal_partial_sum(sequence2, crosses)
    return sum(list(map(max, zip(d1, d2))))
