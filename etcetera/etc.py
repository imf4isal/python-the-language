import os
from ast import arguments
from glob import glob

os.system('cls')
print('\n\n') 

# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3:
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("usage: meows.py [-n NUMBER]")


import argparse

parser = argparse.ArgumentParser(description="Meow like a cat.")
parser.add_argument("-n",default= 1, help= "number of meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")
