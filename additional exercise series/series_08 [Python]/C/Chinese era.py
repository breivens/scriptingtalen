def heavenlyStem(number: int):
    return ('yang ', 'yin ')[number % 2] + ('wood', 'fire', 'earth', 'metal', 'water')[number // 2]


def earthlyBranch(number: int):
    return ('rat', 'buffalo', 'tiger', 'hare', 'dragon', 'snake',
            'horse', 'goat', 'monkey', 'chicken', 'dog', 'pig')[number]


def chineseYear(year: int):
    year += 2697 - (year > 0)
    return f'{heavenlyStem(year % 10)} {earthlyBranch(year % 12)}'
