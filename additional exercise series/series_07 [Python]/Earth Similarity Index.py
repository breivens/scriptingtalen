def ES(obj: list, ref: list, weights=None) -> float:
    n = len(obj)
    weights = weights or [1.0] * n
    assert n == len(ref) == len(weights), 'invalid arguments'
    es = 1.0
    for o, r, w in zip(obj, ref, weights):
        es *= (1 - abs((o - r) / (o + r))) ** (w / n)
    return es


def ESI(r=None, d=None, v=None, t=None):
    earth, weights = [1.00, 1.00, 1.00, 288.0], [0.57, 1.07, 0.70, 5.58]
    # ESI
    if None not in {r, d, v, t}:
        return ES(obj=[r, d, v, t], ref=earth, weights=weights)
    # interior ESI
    if None not in {r, d} and {None} == {v, t}:
        return ES(obj=[r, d], ref=earth[:2], weights=weights[:2])
    # surface ESI
    if None not in {v, t} and {None} == {r, d}:
        return ES(obj=[v, t], ref=earth[2:], weights=weights[2:])
    # invalid
    raise AssertionError('invalid arguments')


# Earth
print(ESI(1.00, 1.00, 1.00, 288.0))
# 1.0

# Mars (interior ESI)
print(ESI(r=0.53, d=0.71))
# 0.8154483513183794

# Mercury (surface ESI)
print(ESI(v=0.38, t=440.0))
# 0.42223988785100186

# Gliese 581g
print(ESI(t=278.0, v=1.51, d=1.22, r=1.36))
# 0.8903703266879102

# Gliese 581g (interior ESI)
print(ESI(d=1.22, r=1.36))
# 0.9021231636588817

# Gliese 581g (surface ESI)
print(ESI(t=278.0, v=1.51))
# 0.878770605369469
