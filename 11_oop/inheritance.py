"""
11 - OOP: Inheritance
----------------------
Inheritance lets a class (child) reuse and extend the behavior of
another class (parent), promoting code reuse.
"""


# --- Parent / Base class ---
class Animal:
    def __init__(self, name, sound="..."):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}"

    def eat(self):
        return f"{self.name} is eating."


# --- Child / Derived class ---
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, sound="Woof")   # call parent constructor
        self.breed = breed

    def fetch(self):
        return f"{self.name} fetches the ball!"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, sound="Meow")
        self.color = color

    def scratch(self):
        return f"{self.name} scratches the post!"


dog = Dog("Rex", "Labrador")
cat = Cat("Whiskers", "black")

print(dog.make_sound())   # inherited method
print(dog.fetch())        # method specific to Dog
print(dog.eat())          # inherited from Animal

print(cat.make_sound())
print(cat.scratch())

# --- Checking inheritance relationships ---
print(isinstance(dog, Animal))   # True
print(isinstance(dog, Dog))      # True
print(isinstance(dog, Cat))      # False
print(issubclass(Dog, Animal))   # True


# --- Multi-level inheritance ---
class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed)

    def play(self):
        return f"{self.name} the puppy is playing!"


puppy = Puppy("Buddy", "Golden Retriever")
print(puppy.make_sound())  # from Animal
print(puppy.fetch())       # from Dog
print(puppy.play())        # from Puppy


# --- Multiple inheritance ---
class Swimmer:
    def swim(self):
        return f"{self.name} can swim!"


class Flyer:
    def fly(self):
        return f"{self.name} can fly!"


class Duck(Animal, Swimmer, Flyer):
    def __init__(self, name):
        super().__init__(name, sound="Quack")


duck = Duck("Donald")
print(duck.make_sound())
print(duck.swim())
print(duck.fly())

# --- Method Resolution Order (MRO) ---
print(Duck.__mro__)

# --- Overriding parent methods ---
class Bird(Animal):
    def eat(self):  # overrides Animal's eat()
        return f"{self.name} pecks at seeds."


bird = Bird("Tweety", sound="Tweet")
print(bird.eat())          # overridden version
print(bird.make_sound())   # inherited, unchanged
