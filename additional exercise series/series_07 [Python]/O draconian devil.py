from functools import reduce
from re import match


def isPrime(n):
    return match(r"^1?$|^(11+?)\1+$", '1' * n) is None


def nPrime(n=10):
    l, m = list(), 100
    while len(l) < n:
        l += filter(isPrime, range(m - 100, m))
        m += 100
    return l[:n]


def anagramHash(phrase, sequence):
    hashtable = dict(zip("abcdefghijklmnopqrstuvwxyz", sequence))
    return reduce(lambda x, y: x * y, map(lambda l: hashtable.get(l, 1), phrase.lower()))


def areAnagrams(phrase1, phrase2, sequence=None):
    if sequence is None:
        sequence = nPrime(26)
    return anagramHash(phrase1, sequence) == anagramHash(phrase2, sequence)


print(anagramHash('Leonardo Da Vinci', nPrime(26)))
print(anagramHash('O Draconian Devil', nPrime(26)))
