student = {}

student["name"] = input("Enter Name: ")
student["age"] = input("Enter Age: ")
student["city"] = input("Enter City: ")

print("\n----- STUDENT INFO -----")

for key, value in student.items():
    print(key, ":", value)