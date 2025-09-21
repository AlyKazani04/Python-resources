#ask for total inputs and print out min max value

total = int(input("Total inputs: "))
num = int(input("Number: "))
largest = num
smallest = num

for i in range(total - 1):
    num = int(input("Number: "))
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest: {0}".format(largest))
print("Smallest: {0}".format(smallest))