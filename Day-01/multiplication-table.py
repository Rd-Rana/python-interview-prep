# Print the multiplication table for a given number.
a = int(input("Enter a number: "))
print("Multiplication Table of", str(a) + ":")
for i in range(1, 11):
    print(a, "x", i, "=", a * i)