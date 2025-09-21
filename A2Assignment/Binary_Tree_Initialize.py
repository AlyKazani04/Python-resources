class node:
    def __init__(self):
        self.Data = ""
        self.LeftPointer = 0
        self.RightPointer = 0

NullPointer = -1
Tree = [node() for i in range(7)]

def InitializeList():
    global RootPointer, FreePointer
    RootPointer = NullPointer
    FreePointer = 0
    for i in range(6):
        Tree[i].LeftPointer = i + 1
        Tree[i].RightPointer = NullPointer
    Tree[6].LeftPointer = NullPointer

InitializeList()

for i in range(7):
    print(Tree[i].LeftPointer, Tree[i].RightPointer)
print(RootPointer)
print(FreePointer)