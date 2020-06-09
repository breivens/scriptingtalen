def reverseTranslation(dictionary: dict):
    rev_dict = dict()
    for key, values in dictionary.items():
        for value in values:
            if value not in rev_dict:
                rev_dict[value] = list()
            rev_dict[value].append(key)
    return {k: sorted(v) for k, v in rev_dict.items()}


print(reverseTranslation({'tension': ['spanning'], 'voltage': ['spanning', 'voltage']}))
print(reverseTranslation({'soul': ['geest', 'gemoed', 'ziel'], 'spirit': ['geest']}))
print(reverseTranslation({'wire': ['draad', 'metaaldraad'], 'thread': ['draad', 'garen']}))
