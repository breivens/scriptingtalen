
while (ins := input()) != "stop":
    x10 = sum(int(ins[i])*(i+1) for i in range(9)) % 11
    print("OK" if (ins[9] == "X" and x10 == 10) or str(x10) == ins[9] else "FOUT")
