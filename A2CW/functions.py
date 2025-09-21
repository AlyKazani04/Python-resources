#void functions= proecedure= no return
#fruitful functions= function= return

def inputOddnumber():
    num = 0
    while num%2==0:
        num = int(input("Input an odd number= "))
    print("You entered correct odd number")

#calling function
inputOddnumber()