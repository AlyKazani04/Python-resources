def InitializeStack():
    global NullPointer, MaxStackSize, Stack, TopPointer
    NullPointer = -1
    MaxStackSize = 10
    Stack = ["" for i in range(MaxStackSize)]
    TopPointer = NullPointer

def Push(Item):
    global TopPointer
    if TopPointer < MaxStackSize-1:
        TopPointer += 1
        Stack[TopPointer] = Item

InitializeStack()

for i in range(10):
    Item = input("Enter: ")
    Push(Item)

for i in range(10):
    print(Stack[i])
