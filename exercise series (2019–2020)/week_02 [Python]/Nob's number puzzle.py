
out = (num1 := input()).center(4)
i = 0
while (num2 := input()) != "-1":
    num1 = str(sum([int(digit) for digit in num1 + num2]))
    out += f"{num2.center(4).rstrip()}\n{(i) * '  '}{num1.center(4)}"
    i += 1

print(out.rstrip())

# EXPLANATION:
# line 8: every loop a new input is requested and stored in the variable num2
# line 9: num1 becomes the sum(of the digits) of the previous number/sum(num1) and the input(num2)
