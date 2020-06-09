count = int(input())
start = int(input())
total_floors = int(input())
up = True if input() == "^" else False
hours = int(input())
minutes = int(input())
verbose = True if input() in ("alles", "verbose") else False

floor = start

for _ in range(count):
    if floor == total_floors:
        up = False

    elif floor == 0:
        up = True

    if floor == start or verbose:
        print("{:02d}:{:02d} {} [{}]".format(hours, minutes, floor, "^" if up else "v"))

    minutes += 1
    hours = (hours + (minutes // 60)) % 24
    minutes %= 60

    floor += 1 if up else -1
