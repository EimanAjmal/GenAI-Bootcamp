class Bird:

    def sound(self):
        print("Bird Sound")


class Sparrow(Bird):

    def sound(self):
        print("Chirp Chirp")


class Parrot(Bird):

    def sound(self):
        print("Hello!")


birds = [Sparrow(), Parrot()]

for bird in birds:
    bird.sound()