class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


student = Student("Eiman", 21)

print(student.name)
print(student.age)
