a = 0
b = 0
op = ''

def welcomeUser():
    print("Welcome to Calculator!")

def thankUser():
    print("Thanks!")

def outputInfo():
    print("Which operation do you want to perform?")
    print("1: Addition (+)")
    print("2: Subtraction (-)")
    print("3: Multiplication (*)")
    print("4: Division (/)")
    print("5: Modulus (%)")
    print("6: Exponentiation (**)")
    print("7: Floor Division (//)")

def inputNumbers():
    global a
    global b
    print()
    a = int(input("Enter number-1: ")) 
    b = int(input("Enter number-2: "))

def inputOperation():
    global op
    op = input("Enter value: ")

def askIfUserWantToContinue():
    print()
    continueOrNot = input("Do you want to continue (y/n)? ")
    while (continueOrNot != 'y' or continueOrNot != 'n'):
        if continueOrNot == 'n':
            thankUser()
            exit(0)
        elif continueOrNot == 'y':
            break
        else:
            print("Please enter valid input.")
            print()
            continueOrNot = input("Do you want to continue (y/n)? ")

welcomeUser()
inputNumbers()
outputInfo()
inputOperation()

while True:
    match op:
        case '1':
            print(a, "+", b, "=", a + b)
        case '2':
            print(a, "-", b, "=", a - b)
        case '3':
            print(a, "*", b, "=", a * b)
        case '4':
            print(a, "/", b, "=", a / b)
        case '5':
            print(a, "%", b, "=", a % b)
        case '6':
            print(a, "**", b, "=", a ** b)
        case '7':
            print(a, "//", b, "=", a // b)
        case _:
            print("Please enter value from 1 to 7 only.")
            outputInfo()
            inputOperation()
            continue

    askIfUserWantToContinue()    
    inputNumbers()
    outputInfo()
    inputOperation()