def translate(word: str, translations: dict):
    translation = translations.get(word.lower(), word)
    return translation.upper() if word.isupper() else translation.title() if word.istitle() else translation.lower()


def sexChange(string: str, translations: dict):
    from re import split as rsplit
    return ''.join([translate(word, translations) for word in rsplit(r'(\W+)', string)])


def undoSexChange(string: str, translations: dict):
    return sexChange(string, {v: k for k, v in translations.items()})
