# arrName = [ [iniVal for i in range(col)] for j in range(row) ]

table = [ [0 for i in range(5)] for j in range(6) ]
for row in range(6):
    for col in range(5):
        print(table[row][col], end=" ")
    print()

# arrName[row][col]

print()
table[1][2] = 2
for row in range(6):
    for col in range(5):
        print(table[row][col], end=" ")
    print()