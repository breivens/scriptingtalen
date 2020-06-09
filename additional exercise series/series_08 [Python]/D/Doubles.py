def double(sequence: list):
    for number in sequence:
        if sequence.count(number) == 2:
            return number
    return None


def doubles(sequence: list):
    once, multiple = set(), set()
    for number in sequence:
        if sequence.count(number) == 1:
            once.add(number)
        else:
            multiple.add(number)
    return once, multiple


print(doubles([2, 8, 8, 6, 10, -20, -4, -2, -4]))
