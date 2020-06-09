def dovetail(cards):
    assert not len(cards) % 2, "aantal kaarten moet even zijn"
    shuffled, mid = [], len(cards) // 2
    for i in range(mid):
        shuffled.append(cards[i])
        shuffled.append(cards[i + mid])
        # or shuffled.extend([cards[i]] + [cards[i + mid]])
    return shuffled


def riffle(cards, repeats=1):
    for _ in range(repeats):
        cards = dovetail(cards)
    return cards


def cycle(n):
    original = list(range(n))
    cards = dovetail(original)
    repeats = 1
    while original != dovetail:
        repeats += 1
        cards = dovetail(cards)
    return repeats
