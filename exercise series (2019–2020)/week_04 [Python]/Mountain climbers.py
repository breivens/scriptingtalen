from itertools import permutations


def is_profile(profile):
    if len(profile) % 2 == 0:  # if alternating and same start-height, the profile can'T even
        return False
    # same start-height / can'T go lower than start / only one summit
    if profile[0] != profile[-1] or min(profile) < profile[0] or profile.count(max(profile)) > 1:
        return False

    for i in range(len(profile) - 1):  # check if alternating high/low
        if profile[i] == profile[i + 1]:
            return False
        if i % 2 == 0 and profile[i] > profile[i + 1]:
            return False
        if i % 2 != 0 and profile[i] < profile[i + 1]:
            return False
    return True


def peak(profile):
    return max(profile)


def levels(profile):
    return sorted(set(profile))


def tussenpunten(profile):
    points = []
    altitudes = levels(profile)
    for h, height in enumerate(profile):
        points.append((height, True))
        if h != len(profile) - 1:
            next_height = profile[h + 1]
            alt = altitudes if height < next_height else altitudes[::-1]
            i = 0
            while alt[i] != next_height:
                if height < alt[i] < next_height:
                    points.append((alt[i], False))
                elif height > alt[i] > next_height:
                    points.append((alt[i], False))
                i += 1
    return points


def contour_lines(profile):
    contour = {p: (set(), set()) for p in profile}
    reached_peak = 0
    for i, item in enumerate(tussenpunten(profile)):
        index_key, boolean = item
        value = tuple((i, boolean))
        if index_key == peak(profile):
            contour[index_key][0].add(value)
            reached_peak = 1
        contour[index_key][reached_peak].add(value)
    return contour


def knots(profile):
    knotted = set()
    for item1, item2 in contour_lines(profile).values():
        item1, item2 = tuple(item1), tuple(item2)
        for i in range(len(item1) * (l := len(item2))):
            p1, b1 = item1[i // l]
            p2, b2 = item2[i % l]
            if b1 or b2:
                knotted.add((p1, p2))
    return knotted


def are_connected(k1, k2, profile):
    points = tussenpunten(profile)
    pointers = [min(k1[0], k2[0]), max(k1[0], k2[0]), min(k1[1], k2[1]), max(k1[1], k2[1])]

    if (pointers[0] - pointers[2]) * (pointers[1] - pointers[3]) < 0 or (
            (pointers[0] - pointers[2]) != (pointers[1] - pointers[3])):
        return False
    pointers[0] += 1
    pointers[2] += 1
    while pointers[0] < pointers[1]:
        if points[pointers[0]][1] or points[pointers[2]][1]:
            return False
        pointers[0] += 1
        pointers[2] += 1
    return True


def connecting_graph(profile):
    connections = {}
    for p1, p2 in set(permutations(knots(profile), 2)):
        if are_connected(p1, p2, profile):
            if p1 in connections:
                connections[p1].add(p2)
            else:
                connections[p1] = {p2}
    return connections
