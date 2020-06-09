def nameword(word: str, names: set):
    word = word.title()
    for name1 in names:
        if word.startswith(name1):
            name2 = word[len(name1):].title()
            if name2 in names:
                return name1 + '-' + name2
    return ''


firstnames = {'Vic', 'Ian', 'Pat', 'Ron', 'Roy', 'Al', 'Tim', 'Jack'}
print(nameword('patron', firstnames))
# 'Pat-Ron'
print(nameword('Victorian', firstnames))
# ''
print(nameword('victim', firstnames))
# 'Vic-Tim'
print(nameword('JACKAL', firstnames))
# 'Jack-Al'
print(nameword('royal', firstnames))
# 'Roy-Al'
print(nameword('herbal', firstnames))
# ''
