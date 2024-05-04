class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = float(age)

    def __str__(self):
        return f"Student {self.name} of age {self.age}"

    def __repr__(self):
        return f"Student({self.name}, {self.age})"