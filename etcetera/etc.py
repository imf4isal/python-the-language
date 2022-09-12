import os
from glob import glob

os.system('cls')
print('\n\n') 

import mypy


def meow(n: int) -> str:
    """
    Meow n times.

    :param n: Number of meow time
    :type n: int
    :raise TypeError
    :return: A string
    :rtype: str
    """
    return "meow\n" * n




number: int = int(input("How many times you want meow?"))

m: str = meow(number)
meow(number)

