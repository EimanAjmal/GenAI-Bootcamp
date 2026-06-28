class Student:

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display(self):
        print("\n----- Student Information -----")
        print("Name :", self.name)
        print("Age  :", self.age)
        print("City :", self.city)


name = input("Enter Name: ")
age = input("Enter Age: ")
city = input("Enter City: ")

student = Student(name, age, city)

student.display()