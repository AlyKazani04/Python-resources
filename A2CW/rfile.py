import pickle
class carRecord:
    def __init__(self):
        self.vehicleID = ""
        self.registration = ""
        self.dateOfregistration = None
        self.engineSize = 0
        self.purchasePrice = 0.0

mycar = carRecord()
mycar.vehicleID = 123
mycar.engineSize = 1000
yourcar = carRecord()
yourcar.vehicleID = 890
yourcar.engineSize = 2000

fileHandle = open("Randcarfile.DAT", "wb+")
address = hash(mycar.vehicleID)
#seek func will find the address of the file
fileHandle.seek(address)
pickle.dump(mycar, fileHandle)
address = hash(yourcar.vehicleID)
fileHandle.seek(address)
pickle.dump(yourcar, fileHandle)
fileHandle.close()

searchID = int(input("enter vehicle id to search"))
fileHandle = open("Randcarfile.DAT", "rb+")
address = hash(searchID)
fileHandle.seek(address)
thiscar = carRecord()
thiscar = pickle.load(fileHandle)
print(thiscar.vehicleID , thiscar.engineSize )
fileHandle.close()