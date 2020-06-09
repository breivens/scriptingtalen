def sequence(n: int, k=0, count=None) -> list:
    seq = [k]
    num = tuple(map(int, str(n)))
    length = len(num)
    for i in range(count - 1 if count else n):
        k += num[i % length]
        seq.append(k)
        if k >= n:
            break
    return seq


def isbelgian(n: int, k=0) -> bool:
    return n in sequence(n, k)


def seeds(n: int) -> list:
    return [k for k in range(n + 1) if isbelgian(n, k)]


def isflemish(n) -> bool:
    return isbelgian(n=n, k=int(str(n)[0]))


def iswestflemish(n) -> bool:
    if isflemish(n):
        num = str(n)
        length = len(num)
        return num == ''.join(map(str, sequence(n=n, k=int(num[0]), count=length)))[:length]
    return False
