
def isISBN(code):
    if not isinstance(code, str):
        return False
    code = code.split("-")
    if tuple(len(el) for el in code) != (1, 4, 4, 1):
        return False
    code = "".join(code)
    if not code[:9].isdigit():
        return False
    x10 = sum(int(code[i])*(i+1) for i in range(9)) % 11
    return (code[9] == "X" and x10 == 10) or str(x10) == code[9]
