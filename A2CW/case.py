#python doesnt have case statements so we use nested ifs using "elif"

Grade = input("Enter your grade.")

if Grade == "A":
    print("Top Grade")
elif Grade == "F" or Grade == "U":
    print("fail")
elif Grade in ("B" , "C" , "D" , "E"):
    print("pass")
else:
    print("Invalid Grade")