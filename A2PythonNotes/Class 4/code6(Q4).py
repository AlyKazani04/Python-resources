#ask for total prime no. and store that many in array

def isPrime(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

total = int(input("Total Prime Numbers: "))
prime = [0 for i in range(total)]
count = 2
index = 0

while prime[total-1] == 0:
    if isPrime(count) == True:
            prime[index] = count
            index += 1
    count +=1

print(prime)


