
print("OK" if (sum([int(input())*(i+1) for i in range(9)]) % 11) == int(input()) else "FOUT")
