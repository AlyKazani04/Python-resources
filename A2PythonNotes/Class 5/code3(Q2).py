# Calc sales for each sales person
# identify highest sale month for each sales person
# Calc avg sales for the entire company for the year

import random

salePerson = int(input("Total Sales Persons: "))
sales = [[0 for i in range(12)] for j in range(salePerson)]

for row in range(salePerson):
    for col in range(12):
        sales[row][col] = random.randint(0, 50)

totalCompany = 0

for row in range(salePerson):
    highest = month = totalPerson = 0
    for col in range(12):
        if sales[row][col] > highest:
            highest = sales[row][col]
            month = col + 1
        totalPerson += sales[row][col]
    avg = totalPerson/12
    totalCompany += totalPerson
    print("Person {0}:".format(row+1))
    print("Best Month: {0}".format(month))
    print("Average Sales: {0}".format(avg))
avg = totalCompany / (salePerson*12)
print("Average Sales for Company: {0}".format(avg))

for row in range(salePerson):
    for col in range(12):
        print(sales[row][col], end=" ")
    print()