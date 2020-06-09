
def isbn_a():  # w/ 10 variables
    a = int(input())
    b = 2*int(input())
    c = 3*int(input())
    d = 4*int(input())
    e = 5*int(input())
    f = 6*int(input())
    g = 7*int(input())
    h = 8*int(input())
    i = 9*int(input())
    print((a+b+c+d+e+f+g+h+i) % 11)

# ---------------------------------------------------------------------------------------------------- #


def isbn_b():  # w/ for-loop
    som = 0
    for i in range(9):
        som += (int(input()) * (i + 1))
    print(som % 11)

# ---------------------------------------------------------------------------------------------------- #


def isbn_c():  # w/ generator
    print(sum([int(input())*(i+1) for i in range(9)]) % 11)
