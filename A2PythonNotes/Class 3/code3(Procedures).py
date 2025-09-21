#void functions = procedures = no return
# fruitful functoins = functions = return
#uses local variables

def inputOddNumber():
    num = 0
    while num%2 == 0:
        num = int(input("Odd Number:"))
    print("Odd no. entered")

#main program

inputOddNumber()