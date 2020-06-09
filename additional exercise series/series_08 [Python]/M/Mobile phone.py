keys = {0: ' ', 2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ'}


def letter2digits(char: str) -> str:
    char = char.upper()
    for i in range(9):
        button = keys.get(i, '')
        if char in button:
            return str(i) * (button.index(char) + 1)
    return ''


def digits2letters(sequence) -> str:
    return keys[int(sequence[0])][len(sequence) - 1]


def codeMultiTap(string: str) -> str:
    digits = prev_digit = ''
    for letter in string:
        digit = letter2digits(letter)
        if set(digit) == set(prev_digit):
            digits += ' '
        digits += digit
        prev_digit = digit
    return digits


def decodeMultiTap(digits: str) -> str:  # faster
    string = group = ''
    for digit in digits:
        if group and digit not in group:
            string += digits2letters(group)
            group = ''
        if digit.isdigit():
            group += digit
    if group:
        string += digits2letters(group)
    return string


def decodeMultiTap2(digits: str):  # slower
    from re import sub, findall
    digits = sub(r'(\d)\1*', lambda m: m.group() + ' ', digits).split()
    return ''.join([digits2letters(sequence) for sequence in digits])
