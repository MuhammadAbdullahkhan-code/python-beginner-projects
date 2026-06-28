"""
11 - OOP: Polymorphism
-----------------------
Polymorphism means "many forms" -- the same method name can behave
differently depending on the object calling it.
"""


# --- Polymorphism via method overriding ---
class Shape:
    def area(self):
        return 0

    def describe(self):
        return f"This shape has an area of {self.area()}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14159 * self.radius ** 2, 2)


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Rectangle(4, 5), Circle(3), Triangle(6, 8)]

for shape in shapes:
    # Same method call, different behavior depending on the object's class
    print(f"{type(shape).__name__}: {shape.describe()}")


# --- Polymorphism with functions (duck typing) ---
class Duck:
    def speak(self):
        return "Quack!"


class Robot:
    def speak(self):
        return "Beep boop!"


def make_it_speak(entity):
    # Doesn't care what type 'entity' is, as long as it has a speak() method
    print(entity.speak())


make_it_speak(Duck())
make_it_speak(Robot())


# --- Polymorphism with built-in functions/operators ---
print(len("hello"))     # works on strings
print(len([1, 2, 3]))    # works on lists
print(len({"a": 1}))     # works on dicts

print(1 + 2)              # int addition
print("a" + "b")          # string concatenation
print([1, 2] + [3, 4])    # list concatenation


# --- Abstract base classes (enforcing a common interface) ---
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        """Subclasses MUST implement this method."""
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


employees = [
    FullTimeEmployee("Faisal", 80000),
    ContractEmployee("Noor", 1500, 40),
]

for emp in employees:
    print(f"{emp.name} earns {emp.calculate_salary()}")

# Employee("Test")   # TypeError: Can't instantiate abstract class
