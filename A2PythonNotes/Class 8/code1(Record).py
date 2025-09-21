# Declare a class without methods to create a class
# all attributes in a record will be public, so it can be directly accessed without methos

class CarRecord:
    def __init__(self):
        self.VehicleID = ""
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.0

# Instantiates a car record

ThisCar = CarRecord()
ThisCar.VehicleID = 1
ThisCar.Registration = "ABC123"
print(ThisCar.VehicleID)
print(ThisCar.Registration)

# array of a record

CarArray = [CarRecord() for i in range(10)]