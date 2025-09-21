def InitializeStack():
    global NullPointer, MaxStackSize, Stack, TopPointer
    NullPointer = -1
    MaxStackSize = 10
    Stack = ["" for i in range(MaxStackSize-1)]
    TopPointer = NullPointer