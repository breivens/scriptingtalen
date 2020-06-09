from re import sub


def tegenzet(order):
    assert len(order) == 3 and sub("[RZ]", "", order) == "", "ongeldige order"
    return ("R" if order[1] == "Z" else "Z") + order[:2]


def score1(order1, order2, game):
    assert (order1 != order2 and len(order1) == len(order2) and
            sub("[RZ]", "", order1 + order2) == "" and
            game.count("R") == game.count("Z") == 26), "ongeldige reeksen"

    set1, set2 = [], []
    while len(game) != 0:
        try:
            if game.index(order1) < game.index(order2):
                set1.append(game[:game.index(order1) + len(order1)])
                game = game[game.index(order1) + len(order1):]
            elif game.index(order1) > game.index(order2):
                set2.append(game[:game.index(order2) + len(order2)])
                game = game[game.index(order2) + len(order2):]
        except ValueError:
            while order1 in game:
                set1.append(game[:game.index(order1) + len(order1)])
                game = game[game.index(order1) + len(order1):]
            while order2 in game:
                set2.append(game[:game.index(order2) + len(order2)])
                game = game[game.index(order2) + len(order2):]
            return len(set1), len(set2)


def score2(order1, order2, game):
    assert (order1 != order2 and len(order1) == len(order2) and
            sub("[RZ]", "", order1 + order2) == "" and
            game.count("R") == game.count("Z") == 26), "ongeldige reeksen"
    score1, score2 = 0, 0
    game_length, order_length = len(game), len(order1)
    i = 0
    while i <= game_length - order_length:
        order = game[i:i + order_length]
        if order == order1:
            score1 += 1
            i += order_length
        elif order == order2:
            score2 += 1
            i += order_length
        else:
            i += 1
    return score1, score2


def winnaar(order1, order2, game):
    s1, s2 = score1(order1, order2, game)
    return 0 if s1 == s2 else (1 if s1 > s2 else 2)
