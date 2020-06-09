
def pytha_a():
    n = int(input())
    for b in range(n, 1, -1):
        for a in range(1, b):
            c = (a**2+b**2)**(1/2)
            if a+b+c == n:
                print((int(a), int(b), int(c)))

# ---------------------------------------------------------------------------------------------------- #


def pytha_b():
    n = int(input())
    for a in range(1, n):
        for b in range(1, n - a):
            if a <= b:
                c = n - a - b
                if a * a + b * b == c * c:
                    print(f"({a:d}, {b:d}, {c:d})")
                    break

# ---------------------------------------------------------------------------------------------------- #


def pytha_c():  # merge of a and b
    n = int(input())
    for b in range(n, 1, -1):
        for a in range(1, b):
            c = n - a - b
            if a**2+b**2 == c**2:
                print((int(a), int(b), int(c)))
                break
