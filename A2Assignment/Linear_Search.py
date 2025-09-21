List = [0 for i in range(50)]
for i in range(50):
    List[i] = i

Found = False
ItemToBeFound = int(input("Number: "))
for i in range(50):
    if List[i] == ItemToBeFound:
        print("Item at index: {0}".format(i))
        Found = True
        break

if Found == False:
    print("Item not in list")