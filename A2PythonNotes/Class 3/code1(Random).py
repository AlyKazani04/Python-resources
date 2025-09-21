#import random
#num = random.randint(1,10)
#print(num)

#generate random num 0-100
#stop at 0
#count and out total num generated

import random
i = 1
num = random.randint(0,100)
while num != 0:
    i += 1
    num = random.randint(0,100)
print(i)
