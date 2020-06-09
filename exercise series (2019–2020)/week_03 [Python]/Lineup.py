
def lineup(people):
    red = [name for name, color in people if color == "R"]
    blue = [name for name, color in people if color == "B"]
    return red + blue[::-1]
