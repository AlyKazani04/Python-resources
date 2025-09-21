def Initialize():
    global NullPointer, MaxSize, FrontPointer, EndPointer, NumInQueue, Queue
    NullPointer = -1
    MaxSize = 10
    FrontPointer = 0
    EndPointer = NullPointer
    NumInQueue = 0
    Queue = ["" for i in range(10)]

def AddItem(Item):
    global NumInQueue, EndPointer
    if NumInQueue < MaxSize:
        EndPointer += 1
        if EndPointer > MaxSize-1:
            EndPointer = 0
        Queue[EndPointer] = Item
        NumInQueue += 1

Initialize()

for i in range(10):
    Item = input("Enter: ")
    AddItem(Item)

for i in range(10):
    print(Queue[i])
