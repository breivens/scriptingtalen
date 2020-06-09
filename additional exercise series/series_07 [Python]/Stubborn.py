def palindrome(string: str, digits=True, other=True, case_sensitive=True) -> bool:
    if False in {digits, other, case_sensitive}:
        new_string = ''
        for char in string:
            if not digits and char.isdigit():  # ignore digits
                continue
            if not other and not char.isalpha():  # ignore non-letter characters
                continue
            if not case_sensitive and char.isupper():  # upper -> lower
                new_string += char.lower()
                continue
            new_string += char
        string = new_string
    return string == string[::-1]


def stubborn(number: int, maximum=1000):
    def reverse(n: int):
        r = 0
        while n > 0:
            r = r * 10 + n % 10
            n //= 10
        return r

    i = 0
    for i in range(maximum):
        number += reverse(number)
        if palindrome(str(number)):
            break
    return i + 1


print(stubborn(871))
print(stubborn(196))
print(stubborn(196, maximum=200))
print(stubborn(78552))
print(stubborn(78552, maximum=25))
