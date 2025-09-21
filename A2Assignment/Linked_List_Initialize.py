# Linked List of 7 nodes

class node:
    def __init__(self):
        self.Data = ""
        self.Pointer = 0

NullPointer = -1
StartPointer = -1
FreePointer = 0
List = [node() for i in range(7)]

def InitializeList():
    for i in range(6):
        List[i].Pointer = i + 1
    List[6].Pointer = NullPointer

InitializeList()

for i in range(7):
    print(List[i].Pointer)
print(NullPointer, StartPointer, FreePointer)
