# take ub and lb from user and print even num between them (exclusive)

ub = int(input("Enter upper bound: "))
lb = int(input("Enter lower bound: "))

if ub % 2 != 0:
    ub = ub - 1
else:
    ub = ub - 2
if lb % 2 != 0:
    lb = lb + 1
else:
    lb = lb + 2

while ub >= lb:
    print(ub)
    ub = ub - 2