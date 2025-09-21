grade = input("Grade:")

if grade == "A":
    print("Top Grade")
elif grade == "F" or grade == "U":
    print("Fail")
elif grade in("B","C","D","E"):
    print("Pass")
else:
    print("Invalid Grade")