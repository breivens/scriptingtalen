def evenOdd(container: iter, even=True) -> list:
    even = 0 if even else 1
    return [x for x in container if x % 2 == even]


inputList = range(10)

print(evenOdd(inputList, even=True))
print(evenOdd(inputList, even=False))
