import random

List = [0 for i in range(50)]
for i in range(50):
    List[i] = random.randint(1, 100)

for i in range(1,50):
    ItemToBeInserted = List[i]
    CurrentItem = i - 1
    while List[CurrentItem] > ItemToBeInserted and CurrentItem > -1:
        List[CurrentItem+1] = List[CurrentItem]
        CurrentItem -= 1
    List[CurrentItem+1] = ItemToBeInserted

for i in range(50):
    print(List[i])
