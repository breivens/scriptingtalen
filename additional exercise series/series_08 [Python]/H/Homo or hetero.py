def homoOrHetero(sequence: list) -> str:
    homo = hetero = False
    visited = set()
    for number in sequence:
        if number in visited:
            homo = True
        if visited and number not in visited:
            hetero = True
        if homo and hetero:
            return 'both'
        visited.add(number)
    return 'homo' if homo else 'hetero' if hetero else 'nothing'


print(homoOrHetero([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]))
# 'homo'
print(homoOrHetero([1, 10, 4, 5, 6, 2, 3]))
# 'hetero'
print(homoOrHetero([10, 9, 8, 10, 2, 10, 4, 6, 3, 7, 5, 4, 4, 7]))
# 'both'
print(homoOrHetero([7]))
# 'nothing'
