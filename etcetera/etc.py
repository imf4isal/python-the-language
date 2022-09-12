import os
from glob import glob

os.system('cls')
print('\n\n') 

import mypy


class Cat:
    MEOW = 3

    def meow(self):
        for _ in range(self.MEOW):
            print("meow")

    


def main():
    cat = Cat()
    cat.meow()




if __name__ == "__main__":
    main()

