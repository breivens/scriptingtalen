def readKey(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        from csv import reader
        output = {columns[0]: columns[1] for columns in reader(file, delimiter=' ')}
    return output


def encode(keymap: dict, plaintext: str, text=""):
    text = "".join(filter(str.isalpha, text.lower()))
    plaintext = "".join(filter(str.isalpha, plaintext.upper()))
    pt_length = len(plaintext) * 5

    if not text:
        from random import choices
        from string import ascii_lowercase
        text = "".join(choices(ascii_lowercase, k=pt_length))

    t_length = len(text)
    plaintext = plaintext.translate(str.maketrans(keymap))

    return "".join(
        [{'a': text[i % t_length].lower(), 'b': text[i % t_length].upper()}[plaintext[i]] for i in range(pt_length)]
    )


def decode(keymap: dict, encoded: str):
    keymap, encoded = {v: k for k, v in keymap.items()}, "".join(['a' if char.islower() else 'b' for char in encoded])
    return "".join([keymap[encoded[i:i + 5]] for i in range(0, len(encoded), 5)])
