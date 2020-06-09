def cipherkey(keytext: str):
    keytext = [char.upper() for char in keytext if char not in (' ', '\t', '\n')]
    key = dict()
    for index, letter in enumerate(keytext):
        if letter not in key:
            key[letter] = list()
        key[letter].append(index + 1)
    return key


def encode(plaintext: str, keytext: str):
    key = cipherkey(keytext)
    index_count = dict.fromkeys(key, 0)
    encoded = list()
    for letter in plaintext.upper():
        key_letter = key[letter]
        encoded.append(key_letter[index_count[letter] % len(key_letter)])
        index_count[letter] += 1
    return encoded


keytext = 'Lost time is never found again.'
print(encode('nondeterminativeness', keytext))
print(encode('interdenominationalism', keytext))
print(encode('gastroenteroanastomosis', keytext))
