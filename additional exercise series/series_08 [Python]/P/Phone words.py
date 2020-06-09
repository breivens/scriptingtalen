def key(word: str) -> str:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    t9 = '22233344455566677778889999'
    return word.upper().translate(str.maketrans(alphabet, t9))


def dictionary(container: list or tuple or set) -> dict:
    dictionary = {}
    for word in container:
        keyword = key(word)
        if keyword not in dictionary:
            dictionary[keyword] = set()
        dictionary[keyword].add(word)
    return dictionary


print(dictionary(['languisher', 'requesters', 'desecrates', 'impostumes', 'recessions', 'fluoresces', 'franchisee',
                  'sequesters', 'holinesses', 'perverters', 'bellyacher', 'succincter', 'encourages', 'refinishes',
                  'lawbreaker', 'blabbering', 'effacement']))
