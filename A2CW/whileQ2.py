#write a prog to find the sum of the digits of a number entered by the user

num = int(input("enter a num:"))
sum = 0

while num != 0:
    num % 10
    sum = sum + num
    num = num//10
print(sum)