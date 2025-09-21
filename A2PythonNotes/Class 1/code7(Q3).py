# write a program to print all prime nums from 0 till user input
num = int(input("Enter Upper Bound: ")) + 1

flag = False
for num in range(2,num):
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    if not(flag):
        print(num)
    flag = False