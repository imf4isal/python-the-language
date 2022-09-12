import os
import random
import re

os.system('cls')
print('\n\n') 

class Hat:
    house = ["Gryffindor", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(f"{name} in {random.choice(cls.house)}")

Hat.sort("Faisal")
