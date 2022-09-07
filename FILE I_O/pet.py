import os

os.system('cls')
print('\n\n') 

# pet_name = input("What's your pet's name? ")

# file = open("petnames.txt", "w")
# file.write(pet_name)
# file.close() #closing the file explicitly.

# here everytime i'm executing the program, the older name is removing. what "w", parameter does is , it rewrite the files every time from the scratch. That's why older name has been removed. In that case, what we can do is using - "a" parameter. a= mean append. It will append the new name into it.


# file = open("petnames.txt", "a")
# file.write(pet_name) # usually it only appends. it will not create any line 
#ronyharryjimmy
#we have to explicitly tell the program to create new line after a name.

# file.write(f"{pet_name}\n") #it will create a new line with every name.
# file.close() #sometimes it's better to forget to use close method. it can create problem. file can be corrupted or deleted. or other problems can be created. we can use other approach to avoid close method.


#new approach #automate the process. it will close for us.

# pet_name = input("What's your pet's name?")

# with open("petnames.txt", "a") as file:
#     file.write(f"{pet_name}\n")


#to read lines

# with open("petnames.txt", "r") as file:
#     lines = file.readlines()

# for line in lines: 
#     # print("hello, ", line) #it's creating 2 new line. one is comes from print by default, another is file's line
#     print("hello, ", line)


# for line in lines: 
#     print("hello, ", line, end="") #we can do this.

# for line in lines: 
#     print("hello, ", line.rstrip()) #better design


#elegant approach
# with open("petnames.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())



# i wanna sort the names. and print those.

# names = []

# with open("petnames.txt", "r") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"hello, {name}")

with open("petnames.txt", "r") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())
