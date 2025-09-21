#ask for total students and create 2 arrays
#one for total marks(out of 50) one for percentage

total = int(input("Total Students: "))
marks = [0 for i in range(total)]
percentage = [0 for i in range(total)]

for i in range(total):
    marks[i] = int(input("Marks Scored: "))
    percentage[i] = marks[i] * 2

print(marks)
print(percentage)
