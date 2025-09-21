import random

fileHandle = open("classFile.txt", "w")
numOfLine = random.randint(1,100)
for i in range(numOfLine):
    val = random.randint(1,10)
    mystr = "Value: " + str(val) + "\n"
    fileHandle.write(mystr)
fileHandle.close()

#read file and count no. of times a value b/w 1-10 was stored

counter = [0 for i in range(10)]

fileHandle = open("classFile.txt", "r")

line = fileHandle.readline()
while len(line) > 0:
    index = int(line[7:]) - 1
    counter[index] += 1
    line = fileHandle.readline()

for i in range(10):
    print("{0}: {1} times".format(i+1, counter[i]))
    