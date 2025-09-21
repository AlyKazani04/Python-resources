import random

fileHandle = open("classFile.txt", 'w')
numOflines = random.randint(1,100)
for i in range(numOflines):
    val = random.randint(1,10)
    mystr = "This line has value " + str(val) + "\n"
    fileHandle.write(mystr)
fileHandle.close()

#read the file and count the num of times each value between 1-10 was stored
#example output would be 
#1:20
#2:5