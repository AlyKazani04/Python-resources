#Q1a
DataArray = [0 for i in range(100)]

#b
def ReadFile():
    global DataArray
    try:
        fileHandle = open("IntegerData.txt" , "r")
        for i in range(100):
            DataArray[i] = fileHandle.readline()
        fileHandle.close()
    except IOError:
        print("File does not exist")
#c
def FindValues():
    global DataArray
    userInput = 0
    while userInput<1 or userInput>100:
        userInput = int(input("Enter a number between 1-100 = "))
    count =0
    for i in range(100):
        if userInput == DataArray[i]:
            count +=1
    return count

def BubbleSort():
    global DataArray
    n=99
    for i in range(99):
        for j in range(n):
            if DataArray[j] > DataArray[j+1]:
                temp = DataArray[j]
                DataArray[j] = DataArray[j+1]
                DataArray[j+1] = temp
        n = n-1

#d
ReadFile()
print("The number of times it appears = " , FindValues())
BubbleSort()
print(DataArray)

#e
