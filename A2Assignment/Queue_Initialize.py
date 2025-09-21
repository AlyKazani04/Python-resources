def Initialize():
    global NullPointer, MaxSize, FrontPointer, EndPointer, NumInQueue, Queue
    NullPointer = -1
    MaxSize = 10
    FrontPointer = 0
    EndPointer = NullPointer
    NumInQueue = 0
    Queue = ["" for i in range(10)]
