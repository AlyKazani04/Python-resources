# ask for total sales person
# take input for sales of each person for 12 months

import random

salePerson = int(input("Total Sales Persons: "))
sales = [[0 for i in range(12)] for j in range(salePerson)]

for row in range(salePerson):
    for col in range(12):
        sales[row][col] = random.randint(0, 50)
 
for row in range(salePerson):
    for col in range(12):
        print(sales[row][col], end=" ")
    print()
