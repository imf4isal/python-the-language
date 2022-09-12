import os
import random
import re

os.system('cls')
print('\n\n') 

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Invalid name.")
        self.name = name


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

student = Student("Harry", "Gryffindor")

print(student)
