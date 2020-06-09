def occurrences(word: str):
    from collections import Counter
    return dict(Counter(filter(str.isalpha, word.lower())))


def isRepetitionWord(word: str, minimal_repetition=1):
    repetitions = set(occurrences(word).values())
    return len(repetitions) == 1 and next(iter(repetitions)) >= minimal_repetition


def repetitionWords(path: str, minimal_repetition=1, minimal_length=1):
    with open(path, 'r', encoding='utf-8') as file:
        wordlist = [line for line in file.read().split('\n') if len(line) >= minimal_length]
    return {word for word in wordlist if isRepetitionWord(word, minimal_repetition)}


print(occurrences('CHACHACHA'))
# {'a': 3, 'h': 3, 'c': 3}
print(occurrences('Esophagographers'))
# {'a': 2, 'e': 2, 'g': 2, 'h': 2, 'o': 2, 'p': 2, 's': 2, 'r': 2}
print(occurrences('happenchance'))
# {'a': 2, 'c': 2, 'e': 2, 'h': 2, 'n': 2, 'p': 2}

print(isRepetitionWord('CHACHACHA'))
# True
print(isRepetitionWord('Esophagographers'))
# True
print(isRepetitionWord('happenchance', minimal_repetition=3))
# False

print(repetitionWords('words.txt', minimal_repetition=2, minimal_length=10))
# {'horseshoer', 'intestines'}
