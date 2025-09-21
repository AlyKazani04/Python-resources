import pickle

class CarRecord:
    def __init__(self):
        self.VehicleID = ""
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.0

MyCar = CarRecord()
MyCar.VehicleID = 123
MyCar.EngineSize = 1000

YourCar = CarRecord()
YourCar.VehicleID = 456
YourCar.EngineSize = 2000

# wb+ = read and write

FileHandle = open("RandCarFile.DAT", "wb+")

Address = hash(MyCar.VehicleID)
# seek func will find address of the file
FileHandle.seek(Address)
pickle.dump(MyCar, FileHandle)

Address = hash(YourCar.VehicleID)
FileHandle.seek(Address)
pickle.dump(YourCar, FileHandle)

FileHandle.close()

SearchID = int(input("Vehicle ID: "))
FileHandle = open("RandCarFile.DAT", "rb")

Address = hash(SearchID)
FileHandle.seek(Address)
ThisCar = CarRecord
ThisCar = pickle.load(FileHandle)
print(ThisCar.VehicleID, ThisCar.EngineSize)
FileHandle.close()
