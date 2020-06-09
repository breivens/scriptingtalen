
numbers = [int(input()) for _ in range(4)]
print("-".join([str(num) for num in numbers]))

while len(set(numbers)) != 1:
    numbers = [abs(numbers[i] - numbers[(i+1) % 4]) for i in range(4)]
    print("-".join([str(num) for num in numbers]))
