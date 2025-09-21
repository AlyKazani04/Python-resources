fileHandle = open("myFile.txt", "r")
line = fileHandle.readline()
while len(line)>0:
    print(line, end="")
    line = fileHandle.readline()

fileHandle.close()