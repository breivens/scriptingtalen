def cryptogram(encoded: str, partial: str):
    decoded, keymap = "", {k: v for k, v in zip(encoded.lower(), partial.lower()) if v != '?'}
    for i, char in enumerate(partial):
        if char == '?':
            encoded_char = encoded[i]
            decoded_char = keymap.get(encoded_char.lower(), char)
            decoded += decoded_char.upper() if encoded_char.isupper() else decoded_char
        else:
            decoded += char
    return decoded


puzzle = 'Qmvrbwlf xwkd iopzlw vf zml pcwvfxzvyl.'
solution = 'Ch?ld??? ??ow fas??r ?n ??? ?p?i?gt?me.'
print(cryptogram(puzzle, solution))
