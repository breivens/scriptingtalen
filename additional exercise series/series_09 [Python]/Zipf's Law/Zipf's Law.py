def zipf(n: int, N: int, l=1.0):
    return n ** -l / sum((n + 1) ** -l for n in range(N))


def readData(path: str, column=1, separator='\t'):
    with open(path, 'r', encoding='utf-8') as file:
        from csv import reader
        content = [int(item[column - 1]) for item in reader(file, delimiter=separator)]
    return content


def testZipf(data, l=1.0):
    data, N, total = sorted(data, reverse=True), len(data), sum(data)
    padding = len(str(N))
    for n, part in enumerate(data):
        n += 1
        print(f"{n}".rjust(padding) +
              f"{part}".rjust(6) +
              f"{zipf(n, N, l):.4f}".rjust(10) +
              f"{part / total:.4f}".rjust(10))


cities = readData('france.txt', 2)
testZipf(cities)
print()
belgium_cities = readData('belgium.txt', 2, ',')
testZipf(belgium_cities, 0.77)
print()
belgium_cities = readData('belgium.txt', 3, ',')
testZipf(belgium_cities, 0.84)
