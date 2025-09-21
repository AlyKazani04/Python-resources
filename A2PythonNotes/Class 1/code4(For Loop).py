# starts at 0
# ends at 10 (10 not included)
for i in range(10):
    print(i)

# 2 parameters: start, end
# end is exclusive
for i in range(4,10):
    print(i, end = "|")
print()

# 3 parameters: start, end, step/iteration
for i in range(10,1,-2):
    print(i, end = " ")
print()