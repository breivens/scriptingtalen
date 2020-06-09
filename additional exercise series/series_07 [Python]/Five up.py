def is_valid_card(card: str):
    from re import match
    return isinstance(card, str) and bool(match("^((([2-9]|10)[cdhsCDHS])|([jqka][cdhs])|([JQKA][CDHS]))$", card))


def string_representation(cards: list):
    assert all(is_valid_card(card) for card in cards), "invalid packet"
    return ' '.join([card if card.isupper() else '**' for card in cards])


def turn_selection(cards: list, selection=None):
    assert all(is_valid_card(card) for card in cards), "invalid packet"
    for i, card in enumerate(cards):
        cards[i] = card.swapcase() if selection is None or i + 1 in selection else card
    return cards


def turn_top(cards: list, index: int):
    assert all(is_valid_card(card) for card in cards), "invalid packet"
    cards[:index] = turn_selection(cards[:index][::-1])
    return cards


def cut(cards: list, index: int):
    assert all(is_valid_card(card) for card in cards), "invalid packet"
    cards[index:], cards[:index] = cards[:index], cards[index:]
    return cards
