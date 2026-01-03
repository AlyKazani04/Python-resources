# Lambda Func syntax:
# keyword = 'lambda'
# lambda (params, ...): "a line of code"

# Advantages and Limitations

# Lambda functions offer several advantages:
# They are concise and can make code more readable for simple operations.
# They’re convenient for small, throwaway functions, especially as arguments to higher-order functions.

# However, they also have limitations:
# They can only contain expressions, not statements.
# They are limited to a single expression, which can make complex operations difficult.
# They can be harder to debug due to their anonymous nature.


# Best Practices

# Use lambda functions when:
# You need a simple function for a short period.
# You’re passing a simple function as an argument to higher-order functions.

# Avoid lambda functions when:
# The operation is complex or requires multiple expressions.
# You need to reuse the function multiple times (define a regular function instead).


square_lambda = lambda x: x ** 2
add = lambda a,b: a + b

print("Lambda Square:", square_lambda(6))
print("Lambda Add:", add(6,5))
# Lambda Square: 36
# Lambda Add: 11

helloworld = lambda: f"Hello World!"

print("Lambda Print:", helloworld())
# Lambda Print: Hello World!

a = lambda: print("call func in lambda")
a()
# call func in lambda

# map func:

# 'map': takes in a func, applies it to a list of items and returns that list
numbers = [1, 2, 3, 4, 5]

squared = list(map(square_lambda, numbers))

print(squared)
# [1, 4, 9, 16, 25]

# filter func:
# 'filter': takes in a func applies it to a list of items and returns only those,- 
# for which the func returned True

evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)
# [2, 4]

# sorted func:
# 'sorted': returns a sorted list based on a key (can take in a func that returns a value as key)
people = [("Aly", 20), ("SomeOneElse", 12), ("SomeOneOtherElse", 79), ("AnotherPerson", 45)]

sorted_people = sorted(people, key=lambda x: x[1])

print(sorted_people)
# [('SomeOneElse', 12), ('Aly', 20), ('AnotherPerson', 45), ('SomeOneOtherElse', 79)]