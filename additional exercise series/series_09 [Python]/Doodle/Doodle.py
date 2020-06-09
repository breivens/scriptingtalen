def activity(path: str, days=1):
    with open(path, 'r', encoding='utf-8') as file:
        schedule = list(filter(None, file.read().split('\n')))

    start, successive, participants = -1, 0, len(schedule)

    for i, day in enumerate([item.count('V') for item in zip(*schedule)]):
        if day == participants:
            successive += 1
            if successive == 1:
                start = i + 1
            if successive == days:
                break
        else:
            start, successive = -1, 0
    return start


print(activity('doodle1.txt'))
print(activity('doodle1.txt', 2))
print(activity('doodle2.txt', 3))
