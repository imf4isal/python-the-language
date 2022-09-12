import os
from ast import arguments
from glob import glob

os.system('cls')
print('\n\n') 


def f(*arg, **kwargs):
    print("positional:", arg)
    print("named:", kwargs)

f(100, 50, 25, name = "Faisal")
