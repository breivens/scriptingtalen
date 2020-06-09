
def a():
    getallen = [0, 0, 0]
    for i in range(3):
        getallen[2-i] = input()
    print(" ".join(getallen))


def b():
    getallen = []
    for i in range(3):
        getallen.append(input())
    print(" ".join(getallen[::-1]))


def c():
    print(" ".join([input() for _ in range(3)][::-1]))

def d():
    a = input()
    b = input()
    c = input()
    print(c, b, a)

def e():
    print(f"{input()[::-1]} {input()[::-1]} {input()[::-1]}"[::-1])


