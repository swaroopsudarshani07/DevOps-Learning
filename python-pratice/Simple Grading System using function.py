
def grading_system(marks):
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Class")
    elif marks >= 50:
        print("Second Class")
    else:
        print("Fail")

score = int(input("Enter marks: "))
grading_system(score)