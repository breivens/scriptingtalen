def encode_a(line):
    new_line, group = "", ""
    for char in line:
        if char.isalpha() and char.lower() not in "aeiou":
            group += char
        elif group:
            new_line += "o" + group.lower()
            group = ""
        new_line += char
    if group:
        new_line += "o" + group.lower()
    return new_line


# noinspection Duplicates

def decode_a(line):
    new_line, count, i = "", 0, 0

    while i < len(line):
        char = line[i]
        if char == 'o' and count > 0:
            i += count
            count = 0
        else:
            if not char.lower() in "aeiou" and char.isalpha():
                count += 1
            new_line += char
        i += 1
    return new_line


print(encode_a('dieventaaltje'))
print(decode_a('dodievoventontaaltjoltje'))

# ---------------------------------------------------------------------------------------------------- #
from re import sub, IGNORECASE


def encode_b(plaintext: str) -> str:
    return sub("[bcdfghjklmnpqrstvwxyz]+", lambda m: m.group() + "o" + m.group().lower(), plaintext, flags=IGNORECASE)


def decode_b(encoded: str) -> str:
    return sub(r"([bcdfghjklmnpqrstvwxyz]+)o\1", r"\1", encoded, flags=IGNORECASE)


print(encode_b('dieventaaltje'))
print(decode_b('dodievoventontaaltjoltje'))
