def readSpecs(path: str):
    specs = dict()
    with open(path, 'r', encoding='utf-8') as file:
        from csv import reader
        reader = reader(file)
        next(reader)  # skip header
        for line in reader:
            color, dig, mult, tol = map(str.lower, line)
            specs[color] = dict()
            for property, value in (('digit', dig), ('multiplier', mult), ('tolerance', tol)):
                if value != '-':
                    specs[color][property] = float(value) if property == 'tolerance' else int(value)
    return specs


def lookup(color: str, property: str, specs: dict):
    color, property = color.lower(), property.lower()
    assert color in specs and property in specs[color], "invalid code"
    return specs[color][property]


def resistance(resistor: str, specs: dict):
    resistor = resistor.lower().split()
    assert len(resistor) >= 3, "invalid code"

    if len(resistor) == 3:
        resistor.append('none')

    digits = "".join([str(lookup(digit, 'digit', specs)) for digit in resistor[:-2]])
    multiplier = lookup(resistor[-2], 'multiplier', specs)
    tolerance = lookup(resistor[-1], 'tolerance', specs)

    strength = int(digits) * 10 ** multiplier

    return f"{strength:.3f}Ω (±{tolerance:.2f}%)"
