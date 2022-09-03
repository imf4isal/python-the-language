import os

os.system('cls')
print('\n\n') 

# https://www.python-engineer.com/posts/string-methods-python/
string = "hello###"

sliced = string[2:6]
#With slicing we can access substrings. It can get optional start and stop indices.


stripped = string.strip('#')
#strip method by default remove leading and trailing whitespace. But we can set chars argument to strip certain characters.
#strip('hello')
#Careful: only leading and trailing found matches are removed:

#similiar method
# lstrip() -remove all occurrences of the passed chars string.
# rstrip() - same right

# print(stripped)
# print('wwww.faisal.com'.strip('cmow.'))

#if we just want to remove the given string, we can use remove prefix and removesuffix.

# list_of_strings = ['string', 'methods', 'in', 'python']

# print(' '.join(list_of_strings))

# print('faisal'.replace('a', 'b'))

# #upper lower
# print('faisal'.upper())
# print('faASal'.upper())
# print('faASal'.lower())
# print('FAISAL'.lower())



#islower,isupper
# print('faisal'.islower())
# print('faisal'.isupper())
# print('Faisal'.isupper())
# print('FAISAL'.isupper())



#isalpha, isnumeric, isalnum
# print('faisal'.isalpha())
# print('faisal'.isnumeric())
# print('faisal'.isalnum())
# print('faisal45'.isalnum())
# print('faisal(8'.isalnum())



#count
# print("faisal".count('a'))

#find - rfind(backward)
# print('faisal'.find('a'))
# print('faisal'.rfind('a'))



#startswith - endswith
# print('faisal'.startswith('f'))
# print('faisal'.endswith('f'))

#partition - only catch first occurance
# print('faisal was awesome'.partition('was'))


#center - ljust - rjust
# print('faisal'.center(20, '-'))

# print('faisal'.ljust(20, '-'))

# print('faisal'.rjust(20, '-'))


#fstring
# name = 'faisal'
# print(f'my name is {name}')

#swapcase()
# print('FaisaL'.swapcase())

#zfill() - fill left with zeros
# print('32'.zfill(5))
# print('-43'.zfill(6))
