#program which accept marks and display grade of student
def DisplayGrade(marks):
    if marks >= 75:
        print("Distinction")
    elif marks >= 60 and marks < 75:
        print("First Class")
    elif marks >= 50 and marks < 60:
        print("Second Class")
    else:
        print("Fail")

def main():
    marks = int(input("Enter marks of student: "))
    DisplayGrade(marks)

if __name__ == "__main__":
    main()