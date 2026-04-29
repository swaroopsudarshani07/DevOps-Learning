# Simple Grading System

# Take marks from the user
marks = int(input("Enter marks: "))

# Use if-elif-else to determine grade
if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 50:
    print("Second Class")
else:
    print("Fail")