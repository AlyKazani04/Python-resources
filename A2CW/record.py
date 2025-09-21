import pickle
#class without methods can be used as a record
#all attributes must be public and can be accessed without methods
class carRecord:
    def __init__(self):
        self.vehicleID = ""
        self.registration = ""
        self.dateOfregistration = None
        self.engineSize = 0
        self.purchasePrice = 0.0
    
mycar = [carRecord() for i in range(100)]
for i in range(100):
    mycar[i].vehicleID = i
    mycar[i].engineSize = 1000 + i
#records can only be stored in binary files
#wb is write binary rb is read binary
fileHandle = open("Carfile.DAT","wb")
for i in range(100):
    #pickle.dump stores record in binary file
    pickle.dump(mycar[i],fileHandle)
fileHandle.close()

thecars = []
fileHandle = open("Carfile.DAT", "rb")
moreline = True
while moreline:
    try:
        thecars.append(pickle.load(fileHandle))
    except EOFError:
        print("file ended")
        moreline = False
fileHandle.close()

for i in range(100):
    print(thecars[i].vehicleID, thecars[i].engineSize)