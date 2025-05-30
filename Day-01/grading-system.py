# Create a grading system:
# Input: marks
# Output: Grade
# 90+ -> A, 75–89 -> B, 60–74 -> C, below 60 -> F
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75 and marks <=89:
    print("Grade: B")
elif marks >= 60 and marks <= 74:
    print("Grade: C")
else:
    print("Grade: F")