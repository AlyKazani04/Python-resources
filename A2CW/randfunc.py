import random
num = random.randint(1,10)
print(num)

#create a program that generates a random number from 1-100
#stops when 0 is generated
#output number of random numbers generated

num1 = random.randint(0,100)
count = 1
while num1 != 0:
    num1 = random.randint(0,100)
    count = count + 1
    print(num1)
print("nums generated" , count) 


