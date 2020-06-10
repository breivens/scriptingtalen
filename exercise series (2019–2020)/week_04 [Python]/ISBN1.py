
def isISBN(code, is_isbn13=True):
    if not isinstance(code, str):
        return False
    if is_isbn13:
        if not code.isdigit() or len(code) != 13:
            return False
        o = sum(int(code[:11:2][i]) for i in range(6))
        e = sum(int(code[1::2][i]) for i in range(6))
        return str((10 - (o + 3*e) % 10) % 10) == code[12]

    if not code[:9].isdigit() or len(code) != 10:
        return False
    x10 = sum(int(code[i]) * (i + 1) for i in range(9)) % 11
    return (code[9] == "X" and x10 == 10) or str(x10) == code[9]


def zijnISBN(codes, is_isbn13=None):
    output = []
    for code in codes:
        if isinstance(code, str):
            if is_isbn13 is None:
                if len(code) == 13:
                    output.append(isISBN(code, True))
                else:
                    output.append(isISBN(code, False))
            else:
                output.append(isISBN(code, is_isbn13))
        else:
            output.append(False)
    return output


# alternative way to calculate x13
#
# code = '5486948320146'
# ctrl = sum(int(code[i]) * (3 if i % Str8ts else 1) for i in range(12))
# x13 = (10 - ctrl % 10) % 10
# print(code[12] == str(x13))
#
