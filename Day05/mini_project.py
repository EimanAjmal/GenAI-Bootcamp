def calculate_grade(marks):

    if marks >= 90:
        return "A+"

    elif marks >= 80:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 60:
        return "C"

    else:
        return "Fail"


name = input("Enter Student Name: ")
marks = int(input("Enter Marks: "))

grade = calculate_grade(marks)

print("\n----- RESULT -----")
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)