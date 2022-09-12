import os
import random
import re

os.system('cls')
print('\n\n') 

class Hat:
    def __init__(self):
        self.house = ["Gryffindor", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(f"{name} in {random.choice(self.house)}")

hat = Hat()
hat.sort("Faisal")
