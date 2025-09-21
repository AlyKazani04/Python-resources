#generate num 1-100 and write code to guess
#max 10 tries

import random
num = random.randint(1,100)
lb = 1
ub = 100
guess = 0
found = False
while found == False:
    mid = (ub+lb)//2
    guess +=1
    if num == mid:
        found = True
    elif num > mid:
        lb = mid + 1
    else:
        ub = ub -1
print(guess, "guesses")
