def merge(chutes: dict, ladders: dict):
    assert (not set(chutes.keys()) & set(ladders.keys()) and
            all(v < k for k, v in chutes.items()) and
            all(k < v for k, v in ladders.items())), "invalid configuration"
    return {k: v - k for k, v in {**chutes, **ladders}.items()}


def spaces(sequence: list or tuple, chutes: dict, ladders: dict):
    token, turns, board = 0, list(), merge(chutes, ladders)
    for roll in sequence:
        if token + roll <= 100:
            token += roll
            token += board.get(token, 0)
        turns.append(token)
    return turns
