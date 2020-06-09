def flip(pancakes: tuple, burnt=False) -> tuple:
    return (tuple(-x for x in pancakes) if burnt else pancakes)[::-1]


def flip_top(pancakes: tuple, m: int, burnt=False) -> tuple:
    return flip(pancakes[:m], burnt) + pancakes[m:]


def find_largest(pancakes: tuple, m: int) -> int:
    return pancakes.index(max(pancakes[:m], key=abs)) + 1


def sorting_step(pancakes: tuple, m: int, burnt=False) -> tuple:
    flipped = flip_top(pancakes, find_largest(pancakes, m), burnt)
    return flip_top(flip_top(flipped, 1, burnt) if burnt and flipped[0] > 0 else flipped, m, burnt)


def sorting_steps(pancakes: tuple, burnt=False) -> list:
    steps = [pancakes]
    for i in range(len(pancakes), 0, -1):
        new_step = sorting_step(steps[-1], i, burnt)
        if new_step != steps[-1]:
            steps.append(new_step)
    return steps
