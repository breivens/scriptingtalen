from collections import Counter
from math import log
from re import sub


def cleanse(text: str):
    return sub("[^a-z]+", "other", text.lower()).strip("other")


def ngrams(text: str, n=1):
    text = cleanse(text)
    return [text[i:i + n] for i in range(len(text) - n + 1)]


def profile(path: str, n=1):
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    return dict(Counter(ngrams(text, n)))


def ngram_count(_profile_: dict):
    return sum(_profile_.values())


def attribution(text: dict, author: dict):
    return -sum(text[ngram] * log((1 + author.get(ngram, 0)) / ngram_count(author)) for ngram in text)


b = profile("bixby.txt", n=3)
print(b)
print(ngram_count(b))

print(attribution(b, profile("lincoln.txt", n=3)))
print(attribution(b, profile("hay.txt", n=3)))
print(attribution(b, profile("obama.txt", n=3)))
