def longShort(table: dict, bound: int) -> tuple:
    long = short = 0
    for key, value in table.items():
        if len(key) < bound:
            short += value
        else:
            long += value
    return long, short
