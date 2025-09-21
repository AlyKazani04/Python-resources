# take input for num and print mult table till 10

num = int(input("Number: "))

for i in range(1,11):
    prod = i * num
    print("{0} x {1} = {2}".format(num, i, prod))