#create a rand num (1-100) and write a program that guesses the num in 10 tries
import random
num = random.randint(1,100)
print("rand num generated=", num)
temp= -1
lower = 0
upper = 100
count = 0
while temp != num:
    temp = (lower + upper)//2
    count += 1
    print("Guess {0} = {1}".format(count,temp))
    if temp > num:
        upper = temp - 1
    elif temp < num:
        lower = temp + 1
print("Total guesses= " , count)