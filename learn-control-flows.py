####################################################
##  Control Flows and Iterables                   ##
##  Basics of if/else, for/while, try/except      ##
##  Basics of iterables                           ##
####################################################

####################################################
## 1. Practice control flows
####################################################

print("\n1. Practice control flows\n")
print("1.1 if/elif/else statements: if (condition) / elif (condition) / else")

# Let's just make a variable
some_var = 5
print(f"1.1.1 some_var = {some_var}")

print(f"1.1.2 check if some_var <10, ==10, >10")
# Here is an if statement. Indentation is significant in Python!
# Convention is to use four spaces, not tabs.
# This prints "some_var is smaller than 10"
if some_var > 10:
    print("1.1.3 if: some_var is totally bigger than 10.")
elif some_var < 10:    # This elif clause is optional.
    print("1.1.3 elif: some_var is smaller than 10.")
else:                  # This is optional too.
    print("1.1.3 else: some_var is indeed 10.")

print("\n1.2 for loops: for elem in [list]")

"""
For loops iterate over lists
prints:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
print("\n1.2.1 for animal in ['dog','cat','mouse']: print(animal) =>")
for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("1.2.1 {} is a mammal".format(animal))

"""
"range(number)" returns an iterable of numbers
from zero up to (but excluding) the given number
prints:
    0
    1
    2
    3
"""
print("\n1.2.2 for i in range(4): print(i)) =>")
for i in range(4):
    print('1.2.2', i)

"""
"range(lower, upper)" returns an iterable of numbers
from the lower number to the upper number
prints:
    4
    5
    6
    7
"""
print("\n1.2.3 for i in range(4,8): print(i)) =>")
for i in range(4, 8):
    print('1.2.3', i)

"""
"range(lower, upper, step)" returns an iterable of numbers
from the lower number to the upper number, while incrementing
by step. If step is not indicated, the default value is 1.
prints:
    4
    6
"""
print("\n1.2.4 for i in range(4, 8, 2): print(i)) =>")
for i in range(4, 8, 2):
    print('1.2.4', i)

"""
Loop over a list to retrieve both the index and the value of each list item:
    0 dog
    1 cat
    2 mouse
"""
print('\n1.2.5 animal = ["dog", "cat", "mouse"]')
print("1.2.5 for i, value in enumerate(animals): print(i, value)) =>")
animals = ["dog", "cat", "mouse"]
for i, value in enumerate(animals):
    print('1.2.5', i, value)


print('\n1.3 while loop: while(condition)')
"""
While loops go until a condition is no longer met.
prints:
    0
    1
    2
    3
"""
print('\n1.3 x = 0')
print('1.3 while x < 4: print(x)')
print('1.3 x += 1 =>')
x = 0
while x < 4:
    print('1.3', x)
    x += 1  # Shorthand for x = x + 1

print('\n1.4 try contol flow: try: \\ except Error as e: \\ else: \\ finally')
# Handle exceptions with a try/except block
try:
    # Use "raise" to raise an error
    raise IndexError("1.4 This is an index error")
except IndexError as e:
    print(e)
    pass                 # Refrain from this, provide a recovery (next example).
except (TypeError, NameError):
    pass                 # Multiple exceptions can be processed jointly.
else:                    # Optional clause to the try/except block. Must follow
                         # all except blocks.
    print("1.4 All good!")   # Runs only if the code in try raises no exceptions
finally:                 # Execute under all circumstances
    print("1.4 We can clean up resources here")


print("\n1.5 with statement: with open('filename') as file:")
import os
os.makedirs('tmp', exist_ok=True) 
# Instead of try/finally to cleanup resources you can use a with statement
'''
with open("myfile.txt") as f:
    for line in f:
        print(line)
'''

contents = {"aa": 12, "bb": 21}
print(f"1.5.1 contents = {contents}")

# Writing to a file
print('\n1.5.2 write to file: with open("myfile1.txt", "w") as f: \
f.write(str(dict))')

with open("tmp/myfile1.txt", "w") as file:
    file.write(str(contents))        # writes a string to a file

print('1.5.3 read file: with open("myfile1.txt") as f: \
c = f.read() \\ print(c)')

# Reading from a file
with open("tmp/myfile1.txt") as file:
    contents = file.read()           # reads a string from a file
print(contents)
# print: {"aa": 12, "bb": 21}

print('\n1.5.4 write to file: with open("myfile2.txt", "w") as f: \
f.write(json.dumps(dict))')

import json
with open("tmp/myfile2.txt", "w") as file:
    file.write(json.dumps(contents))  # writes an object to a file

print('1.5.5 read file: with open("myfile2.txt", "r") as f: \
c = json.load(f) \\ print(c)')

with open("tmp/myfile2.txt", "r") as file:
    contents = json.load(file)       # reads a json object from a file
print(contents)
# print: {"aa": 12, "bb": 21}