"""
11 - OOP: Classes & Objects
----------------------------
Classes are blueprints for creating objects that bundle data (attributes)
and behavior (methods) together.
"""


class Student:
    # --- Class attribute (shared by all instances) ---
    school_name = "City Public School"

    # --- Constructor: runs when a new object is created ---
    def __init__(self, name, age, grade):
        self.name = name        # instance attribute
        self.age = age
        self.grade = grade

    # --- Instance method ---
    def introduce(self):
        return f"Hi, I'm {self.name}, age {self.age}, in grade {self.grade}."

    def have_birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age} years old."

    # --- Special / dunder method: controls how print(object) looks ---
    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, grade={self.grade})"

    # --- Special method: controls how the object looks in lists/debuggers ---
    def __repr__(self):
        return f"Student('{self.name}', {self.age}, '{self.grade}')"


# --- Creating objects (instances) ---
student1 = Student("Ayesha", 16, "10th")
student2 = Student("Usman", 17, "11th")

print(student1.introduce())
print(student2.introduce())

print(student1.have_birthday())

print(student1)          # uses __str__
print(repr(student2))    # uses __repr__

print("School:", Student.school_name)   # accessing class attribute

# --- Class methods and static methods ---
class MathHelper:
    @staticmethod
    def add(a, b):
        """Doesn't need access to the class or instance."""
        return a + b

    @classmethod
    def description(cls):
        """Receives the class itself as the first argument."""
        return f"This is the {cls.__name__} utility class."


print(MathHelper.add(5, 7))
print(MathHelper.description())

# --- Properties (controlled attribute access) ---
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value


circle = Circle(5)
print("Area:", circle.area)
circle.radius = 10
print("New area:", circle.area)

# --- Encapsulation with "private" attributes (convention, not enforced) ---
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # double underscore -> name-mangled, "private"

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
account.deposit(500)
print("Balance:", account.get_balance())
