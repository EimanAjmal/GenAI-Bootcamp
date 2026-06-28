class Employee:

    def __init__(self, name):
        self.name = name

    def work(self):
        print(self.name, "is working.")


class Developer(Employee):

    def work(self):
        print(self.name, "is writing Python code.")


class Designer(Employee):

    def work(self):
        print(self.name, "is designing UI.")


developer = Developer("Eiman")
designer = Designer("Ali")

developer.work()
designer.work()