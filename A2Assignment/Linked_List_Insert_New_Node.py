class node:
    def __init__(self):
        self.Data = ""
        self.Pointer = 0

NullPointer = -1
StartPointer = -1
FreeListPointer = 0

List = [node() for i in range(7)]

def InitializeList():
    for i in range(6):
        List[i].Pointer = i + 1
    List[7].Pointer = NullPointer

print(FreeListPointer)

InitializeList()

for i in range(7):
    print(List[i].Pointer)

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

for i in range(7):
    Item = input("Enter: ")
    InsertNode(Item)

for i in range(7):
    print(List[i].Data, " ", List[i].Pointer)

print(StartPointer)
print(FreeListPointer)