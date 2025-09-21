# Error Handling

NumStr = input("Number: ")

# if try block produces an error, the except block is executed depending on the error type
try:
    Num = int(NumStr)  
    Num = 5/Num

except ValueError:
    print("This is not an integer value")

except ZeroDivisionError:
    print("Division by zero")

else:
    # executed when no except block executed
    print(Num)

finally:
    # this block is always executed
    print("Hi")
