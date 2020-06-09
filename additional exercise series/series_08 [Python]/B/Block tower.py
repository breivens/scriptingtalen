def letters(word: str):
    return sorted(set(word.upper()))


def fragments(word: str):
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in letters(word):
        string = string.replace(char, f"{char} ")
    return string.split()


def block_tower(word: str):
    return tuple(sorted(fragments(word), key=len))


def row_lengths(block_tower: tuple):
    return tuple(map(len, block_tower))


def vowel_positions(block_tower: tuple):
    return {(r, c) for r, row in enumerate(block_tower) for c, column in enumerate(row) if column in 'AEIOU'}


print(letters('Aluminium'))
print(fragments('Aluminium'))
tower = block_tower('Aluminium')
print(tower)
print(row_lengths(tower))
print(vowel_positions(tower))
