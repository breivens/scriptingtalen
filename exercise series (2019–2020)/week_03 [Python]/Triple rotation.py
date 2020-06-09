def category(char):
    if 'a' <= char.lower() <= 'i':
        return 0
    if 'j' <= char.lower() <= 'r':
        return 1
    return 2


def encode(line, k1, k2, k3):
    substrings = ["", "", ""]
    for char in line:
        substrings[category(char)] += char
    encoded, index = "", [k1, k2, k3]
    for char in line:
        cat = category(char)
        substring = substrings[cat]
        encoded += substring[index[cat] % len(substring)]
        index[cat] += 1
    return encoded


def decode(line, k1, k2, k3):
    return encode(line, -k1, -k2, -k3)


# ---------------------------------------------------------------------------------------------------- #

def rotate(ins, n):
    n %= len(ins)
    return ins[n:] + ins[:n]


def my_encode(line, k1, k2, k3):  # inferior lol
    new_line = list(line)
    groups = ["", "", ""]
    indices = [[], [], []]
    for c, char in enumerate(line):
        if char.lower() in "abcdefghi":
            groups[0] += char
            indices[0].append(c)
        elif char.lower() in "jklmnopqr":
            groups[1] += char
            indices[1].append(c)
        else:
            groups[2] += char
            indices[2].append(c)
    indices = indices[0] + indices[1] + indices[2]
    groups = list(rotate(groups[0], k1) + rotate(groups[1], k2) + rotate(groups[2], k3))
    for i, index in enumerate(indices):
        new_line[index] = groups[i]
    return "".join(new_line)
