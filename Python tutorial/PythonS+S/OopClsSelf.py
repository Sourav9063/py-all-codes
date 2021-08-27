class Dog:
    # class object attribute
    species = "Mammal"

    def __init__(self, breed, name, spots):
        self.breedd = breed
        self.namee = name
        self.spotss = spots

    def berk(self):
        print("Oof")


dog = Dog(breed="DSG", name="Name", spots=False)
dog.species = "Change"

print(dog.species)


class Circle:
    pi = 3.1416

    def __init__(self, radius=1):
        """
          Circle class
        """
        self.radius = radius

    def get_circomference(self):
        """Circumference of circle"""
        return self.radius * self.pi * 2


circle = Circle()
print(circle.get_circomference())
circle.radius = 4

# print(circle.())
