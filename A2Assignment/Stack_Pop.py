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

def Pop():
    global TopPointer
    Item = ""
    if TopPointer > NullPointer:
        Item = Stack[TopPointer]
        TopPointer -= 1
    return Item

InitializeStack()

for i in range(10):
    Item = input("Enter: ")
    Push(Item)

for i in range(8):
    print(Pop())

Push("d")
Push("e")
print(Pop())
print(Pop())
