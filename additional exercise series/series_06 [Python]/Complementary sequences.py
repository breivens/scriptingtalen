def increasing(sequence: list or tuple):
    return list(sequence) == sorted(sequence)


def frequencySequence(sequence: list or tuple):
    assert increasing(sequence), "given sequence is not increasing"
    return [sum(1 for item in sequence if item < i + 1) for i in range(sequence[-1] + 1)]


def lift(sequence: list or tuple):
    return [i + 1 + item for i, item in enumerate(sequence)]


def complementarySequences(sequence: list or tuple):
    return lift(sequence), lift(frequencySequence(sequence))
