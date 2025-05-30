# Build a simple game where:
# The computer randomly chooses a number between 1 and 20.
# The user tries to guess the number.
# The program gives hints like "Too high" or "Too low".
# It should keep running until the user guesses correctly.
import random

print("Welcome to Number Guessing Game!")
print()

chosenNumber = random.randrange(1, 21)
print("Computer has randomly chosen a number between 1 and 20.")
print("Now, your turn! Bring your guessing game.")
print()

inputNumber = int(input("Enter a number: "))
hints = 0
while inputNumber != chosenNumber:
    if inputNumber > chosenNumber:
        print("Hint: Too high.")
    elif inputNumber < chosenNumber:
        print("Hint: Too low.")
    hints += 1
    print()
    inputNumber = int(input("Try another number: "))
else:
    print("Congrats! That's correct. You guessed it right in", hints + 1, "attempts." if hints > 0 else "attempt.")