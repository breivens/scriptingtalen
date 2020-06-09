
while (ins := input()) != "stop":
    som = int(ins) + sum(i*int(input()) for i in range(2, 10))
    print("OK" if int(input()) == som % 11 else "FOUT")
