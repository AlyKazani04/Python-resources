def Initialize():
    global NullPointer, MaxSize, FrontPointer, EndPointer, NumInQueue, Queue
    NullPointer = -1
    MaxSize = 10
    FrontPointer = 0
    EndPointer = NullPointer
    NumInQueue = 0
    Queue = ["" for i in range(10)]

def AddItem(Item):
    global NumInQueue, EndPointer , FrontPointer
    if NumInQueue < MaxSize:
        EndPointer += 1
        if EndPointer > MaxSize-1:
            EndPointer = 0
        Queue[EndPointer] = Item
        NumInQueue += 1
    if NumInQueue == 1 :
        FrontPointer = 0

def RemoveItem():
    global NumInQueue, FrontPointer
    Item = ""
    if NumInQueue > 0:
        Item = Queue[FrontPointer]
        NumInQueue -= 1
        if NumInQueue == 0:
            Initialize()
        else:
            FrontPointer += 1
            if FrontPointer >  MaxSize-1:
                FrontPointer = 0
    return Item

Initialize()

for i in range(10):
    Item = input("Enter: ")
    AddItem(Item)

for i in range(8):
    print(RemoveItem())

AddItem("h")
print(RemoveItem())
print(RemoveItem())
print(RemoveItem())
