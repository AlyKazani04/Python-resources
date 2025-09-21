def OutputSpaces(numberOfspaces):
    for i in range(numberOfspaces):
        print(" ", end="")
def OutputSymbol(numberOfsymbols, symbol):
    for i in range(numberOfsymbols):
        print(symbol, end="")
def mixline(numberofspaces, numberofsymbols):
    symbol = str(input("Enter a symbol="))
    OutputSpaces(numberofspaces)
    OutputSymbol(numberofsymbols, symbol)
mixline(5 , 5)