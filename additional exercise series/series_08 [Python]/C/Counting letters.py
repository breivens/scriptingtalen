def countLetters(string: str):
    from collections import Counter
    return ''.join([f'{v}{k}' for k, v in Counter(sorted(string.lower())).items() if k.isalpha()])
