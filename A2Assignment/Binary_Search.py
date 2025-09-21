import random

List = [0 for i in range(50)]
for i in range(50):
    List[i] = random.randint(1, 100)

Swap = False
temp = 0
Index = 49
while Swap == False or Index > 0:
    for j in range(Index):
        if List[j] > List[j+1]:
            temp = List[j]
            List[j] = List[j+1]
            List[j+1] = temp
        Swap = True
    Index = Index - 1

for i in range(50):
    print(List[i])

Found = False
SearchFailed = False
ItemToBeFound = int(input("Number: "))
LowerBound = 0
UpperBound = 49

while Found == False and SearchFailed == False:
    Index = int((LowerBound + UpperBound)/2)
    if List[Index] == ItemToBeFound:
        Found = True
    elif LowerBound >= UpperBound:
        SearchFailed = True
    elif List[Index] > ItemToBeFound:
        UpperBound = Index -1
    else:
        LowerBound = Index + 1

if Found == True:
    print("Item at index: {0}".format(Index))
else:
    print("Item not found")
