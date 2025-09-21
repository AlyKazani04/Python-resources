var = "Hello World"

print(var[3])
print(len(var))

# [start:end]
# runs from start till end - 1
# LEFT
print(var[0:8])

# when end is empty replaces with lenth of the string
# MID
print(var[8:])
print(var[3:8])

# -start means length - start
# RIGHT
print(var[-5:])

# chr gives ASCII char
print(chr(67))

#ord gives ASCII value
print(ord("A"))

# converts string to lower case
print(var.lower())

# converts string to upper case
print(var.upper())

# + with string used to concat
mystr = "hello"
mystr = mystr + " " + var
print(mystr)

# type casting
var = "55"
temp = float(var) + 1
print(temp)
