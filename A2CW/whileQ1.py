#write a program to print first 10 natural numbers in reverse order using a while loop


num = 10
#the loop runs till the condition is true
while num >= 1:
    print(num)
    num = num - 1

#Q) write a program to print all even numbers (eclusive both numbers) entered by the user

lower = int(input("enter lowerbound:"))
upper = int(input("enter upperbound:"))

while upper == lower :
    upper = int(input("enter new upperbound"))

if lower%2 == 0:
    lower = lower + 1
if upper%2 ==0:
    upper = upper + 1

if upper > lower:
    if upper%2 == 0:
        upper = upper - 1
    if lower%2 == 0:
        lower = lower + 1
    while lower < upper:
        if lower%2 == 0:
            print(lower)
        lower = lower + 1

if lower > upper:
    if lower%2 == 0:
        lower = lower - 1
    if upper%2 == 0:
        upper = upper + 1
    while upper < lower:
        if upper%2 ==0:
            print(upper)
        upper = upper + 1