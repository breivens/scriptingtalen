def encode_a(line, key):
    output = ""
    for c, char in enumerate(line):
        if char.isupper():
            output += chr((((ord(char) - 65) + (ord(key[c % len(key)]) - 65)) % 26) + 65)
        else:
            output += char
    return output


def decode_a(line, key):
    output = ""
    for c, char in enumerate(line):
        if char.isupper():
            output += chr((((ord(char) - 65) - (ord(key[c % len(key)]) - 65)) % 26) + 65)
        else:
            output += char
    return output


def encode_b(line, key, sign=1):
    output = ""
    for c, char in enumerate(line):
        if char.isupper():
            output += chr((((ord(char) - 65) + sign * (ord(key[c % len(key)]) - 65)) % 26) + 65)
        else:
            output += char
    return output


def decode_b(line, key):
    return encode_b(line, key, sign=-1)
