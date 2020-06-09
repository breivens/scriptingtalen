def reverse(dictionary: dict):
    return {v: k for k, v in dictionary.items()}


def code39(string: str, key: dict):
    return 's'.join([key[char] for char in string.upper()])


def decode39(string: str, key: dict):
    key = reverse(key)
    return ''.join([key[string[i:i + 9]] for i in range(0, len(string), 10)])
