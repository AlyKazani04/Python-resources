#for loop uses range with 3 parameters
#first parameter is start
#second is end
#third is iteration

#if range has only 1 parameter that is end
#then range starts with 0
for i in range(10):
    print(i , end=" ")

print()

#if range has 2 parameters theyre start and end
for i in range(4,10):
    print(i , end=" ")

print()

#if range has 3 parameters theyre start end and iteration
for i in range(4,20,2):
    print(i , end=" ")

print()

for i in range(-4,20,3):
    print(i , end=" ")
print()


#Q) ask user for a number and output the multplication table (1-10)

num = int(input("Enter a number"))
for i in range(1,11):
    print(num , "x" , i ,"=" , num*i)

#ask user for total inputs, take that many inputs
#output the largest and smallest value

n = int(input("total inputs="))
max = int(input("enter a num"))
min = max
for i in range(0,n-1):
    x = int(input("enter a num"))
    if x > max:
        max = x
    if x < min:
        min = x
print("max is" , max)
print("min is" , min)

#ask user for the max number and output all the prime numbers from 1 to max

maximum = int(input("enter a num"))
for num in range(1, maximum + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
            
    else :
        print(num)