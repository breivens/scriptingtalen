def digits2letters(digits: str, letters: str):
    return dict(zip(digits, letters))


def beghilosz2text(digits: str, digits2letters: dict):
    return digits.translate(str.maketrans(digits2letters))[::-1]


def letters2digits(digits2letters: dict):
    return {v: k for k, v in digits2letters.items()}


def text2beghilosz(letters: str, letters2digits: dict):
    for char in letters:
        if char not in letters2digits and char.swapcase() in letters2digits:
            letters = letters.replace(char, char.swapcase())
    return letters.translate(str.maketrans(letters2digits))[::-1]


c2l = digits2letters('012345678', 'OIZEhSgLB')
print(c2l)
print(beghilosz2text('250714638', c2l))
# 'BEghILOSZ'
print(beghilosz2text('3722145', c2l))
# 'ShIZZLE'
print(beghilosz2text('53177187714', c2l))
# 'hILLBILLIES'
l2c = letters2digits(c2l)
print(l2c)
print(text2beghilosz('BEghILOSZ', l2c))
# '250714638'
print(text2beghilosz('SHIZZLE', l2c))
# '3722145'
print(text2beghilosz('hillbillies', l2c))
# '53177187714'
