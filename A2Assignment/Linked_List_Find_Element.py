def InitializeList():
    for i in range(6):
        List[i].Pointer = i + 1
    List[6].Pointer = NullPointer

def InsertNode(Item):
    global StartPointer, FreeListPointer
    if NullPointer != FreeListPointer:
        NewNodePointer = FreeListPointer
        List[NewNodePointer].Data = Item
        FreeListPointer = List[FreeListPointer].Pointer
        ThisNodePointer = StartPointer
        PreviousNodePointer = ThisNodePointer
        while ThisNodePointer != NullPointer and List[ThisNodePointer].Data < Item:
            PreviousNodePointer = ThisNodePointer
            ThisNodePointer = List[ThisNodePointer].Pointer
        if ThisNodePointer == StartPointer:
            List[NewNodePointer].Pointer = StartPointer
            StartPointer = NewNodePointer
        else:
            List[NewNodePointer].Pointer = List[PreviousNodePointer].Pointer
            List[PreviousNodePointer].Pointer = NewNodePointer

class node:
    def __init__(self):
        self.Data = ""
        self.Pointer = 0

NullPointer = -1
StartPointer = -1
FreeListPointer = 0
List = [node() for i in range(7)]

InitializeList()

InsertNode("c")
InsertNode("d")
InsertNode("b")
InsertNode("f")
InsertNode("a")
InsertNode("g")
InsertNode("e")


def FindNode(Item):
    CurrentNodePointer = StartPointer
    while CurrentNodePointer != NullPointer and List[CurrentNodePointer].Data != Item:
        CurrentNodePointer = List[CurrentNodePointer].Pointer
    return CurrentNodePointer

for i in range(7):
    print(List[i].Data, " ", List[i].Pointer)
print(StartPointer)

print(FindNode("g"))