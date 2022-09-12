import os
import random
import re

os.system('cls')
print('\n\n') 

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("name: ")
        house = input("house: ")
        return cls(name, house)

student = Student.get()
print(student)
