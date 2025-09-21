# sequential file processing
# pickle is a library that handles binary files

import pickle

class CarRecord:
    def __init__(self):
        self.VehicleID = ""
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.0

MyCars = [CarRecord() for i in range(100)]
for i in range(100):
    MyCars[i].VehicleID = i

# records can only be stored in binary files
# varName = open(FileName, mode)
# wb = write binary
# rb = read binary

FileHandle = open("CarFile.DAT", "wb")
for i in range(100):
    #pickle.dump stores record in binary file
    pickle.dump(MyCars[i], FileHandle)

FileHandle.close()

TheCars = []
FileHandle = open("CarFile.DAT", "rb")
MoreLines = True

while MoreLines:
    try:
        #pickle.load will read the binary line from file
        TheCars.append(pickle.load(FileHandle))
    except EOFError:
        print("File ended")
        MoreLines = False
FileHandle.close()

for i in range(100):
    print(TheCars[i].VehicleID, TheCars[i].EngineSize)
