#ask user for total prime numbers required
#store that many primes in an array starting from 2

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


num = int(input("enter number of primes needed="))
primes = [0 for i in range(num)]
count = 2
for i in range(num):
    while isprime(count) == False:
        count += 1
    primes[i] = count
    count += 1
print(primes)