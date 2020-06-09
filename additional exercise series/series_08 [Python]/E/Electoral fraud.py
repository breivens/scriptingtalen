def doubles(sequence: list) -> list:
    return sorted({item for item in sequence if sequence.count(item) > 1})


print(doubles([3, 9, 4, 3, 8, 7, 3, 4, 2]))
# [3, 4]
print(doubles([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# []
print(doubles([8, 6, 9, 5, 7, 4, 8, 3]))
# [8]
print(doubles(['0476-987394', '0498-837493', '0476-987394']))
# ['0476-987394']
