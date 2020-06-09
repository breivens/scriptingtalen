def magicWord(sequence: list, word: str) -> bool:
    mapping = {}
    for i, char in enumerate(word):
        number = sequence[i]
        if char not in mapping and number not in mapping:
            mapping[char] = number
            mapping[number] = char
        elif mapping.get(char) != number or mapping.get(number) != char:
            return False
    return True


print(magicWord([9, 23, 14, 14, 18, 5], 'winner'))
# True
print(magicWord([9, 23, 14, 14, 18, 5], 'looser'))
# False
print(magicWord([9, 23, 14, 14, 18, 5], 'zipper'))
# True
print(magicWord([9, 23, 14, 14, 18, 5], 'hummus'))
# False
