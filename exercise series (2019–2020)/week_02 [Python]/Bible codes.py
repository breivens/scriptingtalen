from re import sub


def for_loop():  # second slowest
    start, step, length = int(input()) - 1, int(input()), int(input())
    verse = ""

    while line := input():
        verse += line

    for char in verse:
        if not char.isalpha():
            verse = verse.replace(char, "")

    word = verse[start::step]

    print(f"{word[:length] if len(word) > length else word + (length - len(word)) * '?'}")


def alt_w_for_loop():  # slowest
    start, step, length = int(input()) - 1, int(input()), int(input())
    verse = ""

    while line := input():
        verse += line

    verse = ''.join(char for char in verse if char.isalpha())
    word = verse[start::step]

    print(f"{word[:length] if len(word) > length else word + (length - len(word)) * '?'}")


def filter_func():  # second fastest
    start, step, length = int(input()) - 1, int(input()), int(input())
    verse = ""

    while line := input():
        verse += line

    verse = "".join(filter(str.isalpha, verse))
    word = verse[start::step]

    print(f"{word[:length] if len(word) > length else word + (length - len(word)) * '?'}")


def regex_sub():  # fastest
    start, step, length = int(input()) - 1, int(input()), int(input())
    verse = ""

    while line := input():
        verse += line

    verse = sub("[^a-zA-Z]", "", verse)
    word = verse[start::step]

    print(f"{word[:length] if len(word) > length else word + (length - len(word)) * '?'}")
