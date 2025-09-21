#calculate sum of digits of a number

nums = input("Enter number: ")
numi = int(nums)
length = 0
total = 0

while numi >= 1:
    length += 1
    numi = numi / 10

for i in range(length):
    total = total + int(nums[i])
print(total)

# alternate way

for i in range(5):
    print()

num = int(input("Enter number: "))
sum = 0

while num != 0:
    rem = num % 10
    sum = sum + rem
    num = num // 10

print(sum)






