from re import split as rsplit

numbers, units, exponents = '零一二三四五六七八九', '千百十', '万億兆京垓秭穣溝澗正載極'


# noinspection Duplicates
def vanJapans(n):  # second slowest
    myriads = n.translate(str.maketrans(numbers, '0123456789'))
    myriads = rsplit(f'[{exponents}]', myriads)
    for m, myriad in enumerate(myriads):
        if myriad:
            if myriads[m][0] in '千百十':
                myriads[m] = '1' + myriads[m]
            if '千百' in myriads[m]:
                myriads[m] = myriads[m][:2] + '1' + myriads[m][2:]
            if '百十' in myriads[m]:
                myriads[m] = myriads[m][:4] + '1' + myriads[m][4:]
            if '千' not in myriads[m]:
                myriads[m] = '0千' + myriads[m]
            if '百' not in myriads[m]:
                myriads[m] = myriads[m][:2] + '0百' + myriads[m][2:]
            if '十' not in myriads[m]:
                myriads[m] = myriads[m][:4] + '0十' + myriads[m][4:]
            myriads[m] = myriads[m].ljust(7, '0')
        else:
            myriads[m] = "0000"
    return int("".join(filter(str.isdigit, "".join(myriads))))


# noinspection Duplicates
def vanJapansAlt(n):  # fastest
    myriads = n.translate(str.maketrans(numbers, '0123456789'))
    myriads = rsplit(f'[{exponents}]', myriads)
    for m, myriad in enumerate(myriads):
        if myriad:
            if myriads[m][0] in '千百十':
                myriads[m] = '1' + myriads[m]
            if '千百' in myriads[m]:
                myriads[m] = myriads[m][:2] + '1' + myriads[m][2:]
            if '百十' in myriads[m]:
                myriads[m] = myriads[m][:4] + '1' + myriads[m][4:]
            if '千' not in myriads[m]:
                myriads[m] = '0千' + myriads[m]
            if '百' not in myriads[m]:
                myriads[m] = myriads[m][:2] + '0百' + myriads[m][2:]
            if '十' not in myriads[m]:
                myriads[m] = myriads[m][:4] + '0十' + myriads[m][4:]
            myriads[m] = myriads[m].ljust(7, '0')
        else:
            myriads[m] = "0000"
    return int("%".join(myriads)[::2])


# noinspection Duplicates
def vanJapans2(string):  # second fastest
    number, myriad, n = 0, 0, 0
    for c in string:
        if c in numbers:
            number = numbers.index(c)
        elif c in units:
            number = 1 if number == 0 else number
            myriad += number * 10 ** (3 - units.index(c))
            number = 0
        else:
            n += (myriad + number) * 10 ** (4 * (exponents.index(c) + 1))
            number, myriad = 0, 0
    n += myriad + number
    return n

# noinspection Duplicates
def vanJapans3(string):  # slowest
    # dict(zip(numbers + units, [f"+{i}" for i in range(10)] + ['*1000', '*100', '*10']))
    d = {'零': '+0', '一': '+1', '二': '+Str8ts', '三': '+3', '四': '+4', '五': '+5', '六': '+6', '七': '+7', '八': '+8', '九': '+9',
         '千': '*1000', '百': '*100', '十': '*10'}
    myriads = rsplit(f'[{exponents}]', "".join(map(lambda l: d.get(l, l), string)))
    return "".join(map(lambda l: str(eval(l.strip("+*"))) if l else '0000', myriads))
