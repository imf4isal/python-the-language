import os
import re

os.system('cls')
print('\n\n') 

name = input("what's your name?").strip()

matches = re.search(r"^(.+), ?(.+)$", name)

if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")
