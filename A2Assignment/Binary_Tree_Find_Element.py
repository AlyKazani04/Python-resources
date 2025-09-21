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

def InsertNode(Item):
    global FreePointer, RootPointer
    if FreePointer != NullPointer:
        NewNodePointer = FreePointer
        FreePointer = Tree[FreePointer].LeftPointer
        Tree[NewNodePointer].Data = Item
        Tree[NewNodePointer].LeftPointer = NullPointer
        Tree[NewNodePointer].RightPointer = NullPointer
        if RootPointer == NullPointer:
            RootPointer = NewNodePointer
        else:
            ThisNodePointer = RootPointer
            while ThisNodePointer != NullPointer:
                PreviousNodePointer = ThisNodePointer
                if Tree[ThisNodePointer].Data > Item:
                    TurnedLeft = True
                    ThisNodePointer = Tree[ThisNodePointer].LeftPointer
                else:
                    TurnedLeft = False
                    ThisNodePointer = Tree[ThisNodePointer].RightPointer
            if TurnedLeft == True:
                Tree[PreviousNodePointer].LeftPointer = NewNodePointer
            else:
                Tree[PreviousNodePointer].RightPointer = NewNodePointer

InitializeList()

InsertNode("g")
InsertNode("h")
InsertNode("d")
InsertNode("n")
InsertNode("a")
InsertNode("s")
InsertNode("x")

def FindNode(Item):
    ThisNodePointer = RootPointer
    while ThisNodePointer != NullPointer and Tree[ThisNodePointer].Data != Item:
        if Tree[ThisNodePointer].Data > Item:
            ThisNodePointer = Tree[ThisNodePointer].LeftPointer
        else:
            ThisNodePointer = Tree[ThisNodePointer].RightPointer
    return ThisNodePointer

print(FindNode("s"))
print(FindNode("a"))
