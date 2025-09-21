#read the file and count the num of times each value between 1-10 was stored
#example output would be 
#1:20
#2:5
fileHandle = open("classFile.txt", "r")
count= [0 for i in range(10)]
oneLine = fileHandle.readline()
print(oneLine[20:])
b = oneLine[20:]
while len(oneLine)>=0:
    index = int(b) -1
    count[index] += 1
    oneLine = fileHandle.readline()
for i in range(10):
    print("{0}: {1}".format(i+1,count[i]))
fileHandle.close()