def update(num1, num2, num3):
    num1 += 1
    num2 = num2 * 2
    num3 = num3 - 1
    return num1, num2, num3

var1 , var2, var3 = update(6,5,0)
print(var1,var2,var3)

#create a function that takes a number as parameter and returns
#true if it is even

def iseven(num):
    if num%2 == 0:
        return "True"
    else :
        return "False"
var= iseven(5)
print(var)

#create a function that takes a number as a parameter and returns
#true is the number is prime otherwise false
def isprime(num):
    if num == 2:
        return True
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
            return False
           else:
            return True
    else:
        return "Enter a positive integer greater than 1"
vari = isprime(0)                  
print(vari)