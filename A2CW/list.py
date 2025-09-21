#arrayname = [initval for i in range(size o array)]
list1 = [1 for i in range(10)]  
print(list1)
list1[0] = 2
print(list1)
list1[4] = 9
print(list1[4])

#ask user for total students
#create array and take input for marks of each student out of 50
#create array and calculate percentage and store

stds = int(input("Input number of students="))
arraymarks = [0 for i in range(stds)]
for i in range(stds):
    var = int(input("Enter marks= "))
    arraymarks[i] = var
arraypercentage = [0 for i in range(stds)]
for i in range(stds):
    arraypercentage[i] = arraymarks[i] * 2
print("marks obtained= " , arraymarks)
print("percentages= " , arraypercentage)
