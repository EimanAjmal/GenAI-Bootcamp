class Animal:

    def speak(self):
        print("Animal Sound")


class Cat(Animal):

    def speak(self):
        print("Meow")


cat = Cat()

cat.speak()