# Take input of three numbers and print the greatest.
a = int(input("Enter number-1: "))
b = int(input("Enter number-2: "))
c = int(input("Enter number-3: "))
if a > b:
    if a > c:
        print("Max =", a)
    else:
        print("Max =", c)
else:
    if b > c:
        print("Max =", b)
    else:
        print("Max =", c)