def roman2arab(numeral: str):
    table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return sum(
        [-table[num] if n < len(numeral) - 1 and table[numeral[n]] < table[numeral[n + 1]] else
         table[num] for n, num in enumerate(numeral)])


def arab2roman(integer: int):
    roman, table = "", {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
                        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    for unit in table:
        while integer >= unit:
            integer -= unit
            roman += table[unit]
    return roman


class Roman:
    def __init__(self, value: int or str):
        if isinstance(value, str):
            value = value.upper()
            assert set(value) <= {'M', 'I', 'L', 'C', 'X', 'V', 'D'}, "invalid roman numeral"
            self.number = roman2arab(value)
        else:
            assert isinstance(value, int) and 1 <= value <= 4000, "invalid roman numeral"
            self.number = value

    def __repr__(self):
        return arab2roman(self.number)

    def __int__(self):
        return self.number

    def __add__(self, other):
        return Roman(self.number + other.number)

    def __sub__(self, other):
        return Roman(self.number - other.number)

    def __mul__(self, other):
        return Roman(self.number * other.number)
