numStr = input("enter a number")
try:
    num = int(numStr)
    num = 5/num
except ValueError:
    print("this is not an integer value")
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print(num)
finally:
    #this block executes no matter what
    print("see this works")