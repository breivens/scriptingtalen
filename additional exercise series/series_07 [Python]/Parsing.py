def onlyletters(s: str) -> str:
    return ''.join(filter(str.isalpha, s))


def doublehyphen(s: str) -> bool:
    from re import search
    return bool(search('[^-]--[^-]', s))


def wordlist(s: str) -> list:
    words = []
    for word in s.split():
        if doublehyphen(word):
            words.extend([onlyletters(w).lower() for w in word.split('--')])
        else:
            words.append(onlyletters(word).lower())
    return words


def numberofwords(s: str, l: list) -> list:
    return [s, l.count(s)]


def uniquewords(l: list) -> list:
    return sorted({w.lower() for w in l})


def longestword(l: list) -> int:
    return max(map(len, l))
