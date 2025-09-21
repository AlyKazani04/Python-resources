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
