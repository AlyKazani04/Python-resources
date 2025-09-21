fileHandle = open("myfile.txt" , "r")
oneline = fileHandle.readline()
while len(oneline)>=0:
    print(oneline,end="")
    oneline = fileHandle.readline()

fileHandle.close()