# Ask the user for their name and age, and print a message like:
# "Hello Alice, you will turn 100 years old in the year 2090."
name = input("Enter your name: ")
age = int(input("Enter your age: "))
currentYear = 2025
hundredAgeYear = str((currentYear - age) + 100)
print("Hello " + name + ", you will turn 100 years old in the year " + hundredAgeYear + ".")