# create func that returns true when parameter is prime

def isPrime(num):
    flag = True
    for i in range(2, num):
        if num%i == 0:
            flag = False
    if num <= 1:
        flag = False
    return flag
    
print(isPrime(1))
print(isPrime(2))
print(isPrime(5))
print(isPrime(23))