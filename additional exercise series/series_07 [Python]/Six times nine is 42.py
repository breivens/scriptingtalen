def evaluation(exp: str, base: int) -> int:
    from re import sub
    return eval(sub('[0-9]+', lambda m: str(int(m.group(), base)), exp))


def numeralSystem(exp: str) -> int:
    bases, (left, right) = [], exp.split('=')
    for b in range(2, 37):
        try:
            if evaluation(exp=left, base=b) == evaluation(exp=right, base=b):
                bases.append(b)
        except ValueError:
            continue
    return min(bases)


print(numeralSystem('6 * 9 = 42'))
print(numeralSystem('17 + 33 * 56 = 41 * 42'))
