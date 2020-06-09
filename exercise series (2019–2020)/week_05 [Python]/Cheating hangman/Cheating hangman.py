from collections import Counter
from random import choice


def candidate(word, pattern, suggested):
    if len(word) != len(pattern):
        return False
    for i, char in enumerate(pattern):
        if char == 'other' and word[i] in suggested:
            return False  # char guessed but still empty
        if char != 'other' and (char != word[i] or char not in suggested):
            return False  # pattern not like word or added before suggested
    return True


def fill(word, pattern, letter):
    return "".join(word[i] if word[i] == letter else pattern[i] for i in range(len(word)))


def select(pattern, suggested, letter):
    with open('words.txt', "r") as file:
        content = file.read()
    # all candidates
    candidates = [line.strip() for line in content.split("\n") if candidate(line.strip(), pattern, suggested)]
    # all patterns with the letter added
    patterns = [fill(c, pattern, letter) for c in candidates]
    # most common pattern is chosen as the new pattern
    new_pattern = Counter(patterns).most_common(1)[0][0]
    # a random candidate is chosen from those with the new pattern
    return new_pattern, choice([c for c in candidates if candidate(c, new_pattern, suggested + letter)])
