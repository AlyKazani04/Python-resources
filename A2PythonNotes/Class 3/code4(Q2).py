#create func mixline() that takes two parametres
# num of spaces and num of symbols
#func will call other funcs

def mixline(spaceCount, symbolCount):
    outputSpace(spaceCount)
    outputSymbol(symbolCount)

def outputSpace(count):
    for i in range(count):
        print(" ", end="")

def outputSymbol(count):
    for i in range(count):
        print("*", end="")

mixline(5,5)