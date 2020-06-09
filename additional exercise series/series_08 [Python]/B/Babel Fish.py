def addTranslation(word: str, translation: str, wordlist: dict):
    wordlist[word] = translation


def translation(word: str, wordlist: dict):
    return wordlist.get(word, '???')
