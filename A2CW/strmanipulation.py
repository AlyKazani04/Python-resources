var = "This is Cedar College"

print(var[5])
print(len(var))
#[start:end]
#runs till end - 1
#Left func
print(var[0:6])
#Mid func
print(var[6:])
#when start is - , length - start
#Right func
print(var[-4:])

#chr gives ascii char
print(chr(67))
#ord gives ascii value
print(ord("a"))
#converts str to lower
print(var.lower())
#converts str to upper
print(var.upper())

#+ with str concats 
mystr = "HELLO"
mystr = mystr + " " + var
print(mystr)

#type casting
var = "55"
temp = int(var) + 1
print(temp)

var = "55"
temp = float(var) + 1
print(temp)