####################################################
##  Control Flows and Iterables                   ##
##  Basics of if/else, for/while, try/except      ##
##  Basics of iterables                           ##
####################################################

####################################################
## 1. Practice control flows
####################################################

print("\n1. Control Flows\n")
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

print("\n1.2 For loops iterate over lists: for elem in [list]")

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
print("\n1.2.2 range(x) returns an iterable of numbers from zero up to \n\
(but excluding) x")
print("1.2.2 for i in range(4): print(i)) =>")
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
print("\n1.2.3 range(lower, upper) returns an iterable of numbers \n\
from the lower number to the upper number")
print("1.2.3 for i in range(4,8): print(i)) =>")
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
print("\n1.2.4 range(lower, upper, step) returns an iterable of numbers \n\
from the lower number to the upper number, while incrementing \n\
by step (default is 1).")
print("1.2.4 for i in range(4, 8, 2): print(i)) =>")
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
print('1.3 While loops go until a condition is no longer met.')
print('1.3 x = 0')
print('1.3 while x < 4: print(x)')
print('1.3 x += 1 =>')
x = 0
while x < 4:
    print('1.3', x)
    x += 1  # Shorthand for x = x + 1

print('\n1.4 Handle exceptions with a try/except block')
print('1.4 try contol flow: try: \\ except Error as e: \\ else: \\ finally')
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


print("\n1.5 Instead of try/finally to cleanup resources \
you can use a with statement")

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

print('\n1.5.4 write to file: with open("myfile2.txt", "w") as f: \n\
1.5.4   f.write(json.dumps(dict))')

import json
with open("tmp/myfile2.txt", "w") as file:
    file.write(json.dumps(contents))  # writes an object to a file

print('1.5.5 read file: with open("myfile2.txt", "r") as f: \n\
1.5.5   c = json.load(f) \\ print(c)')

with open("tmp/myfile2.txt", "r") as file:
    contents = json.load(file)       # reads a json object from a file
print(contents)
# print: {"aa": 12, "bb": 21}

####################################################
## 1. Iterables
####################################################

print("\n2. Iterables")
print("2.1 Python offers a fundamental abstraction called the Iterable. \n\
An iterable is an object that can be treated as a sequence. \n\
The object returned by the range function, is an iterable.")

filled_dict = {"one": 1, "two": 2, "three": 3}
print(f"\n2.2 filled_dict = {filled_dict}")
our_iterable = filled_dict.keys()
# dict_keys(['one', 'two', 'three']). This is an object
# that implements our Iterable interface.
print("2.2.1", our_iterable)  

# We can loop over it.
print("2.2.2 We can loop over it =>")
for i in our_iterable:
    print("2.2.3", i)  # Prints one, two, three

# However we cannot address elements by index.
print("\n2.3 However we cannot address elements by index.")
try:
    our_iterable[1]  # Raises a TypeError
except TypeError as e:
    print("2.3.1 TypeError with our_iterator[1]")
else:
    print("2.3.1 No error with our_iterator[1]")

print("\n2.4 An iterable is an object that knows how to create an iterator.")
print("2.4.1 our_iterator = iter(our_iterable)")
# An iterable is an object that knows how to create an iterator.
our_iterator = iter(our_iterable)

# Our iterator is an object that can remember the state as we traverse through
# it. We get the next object with "next()".
print("\n2.5 Our iterator is an object that can remember the state as we \n\
traverse through it. We get the next object with next()")
print("2.5.1", next(our_iterator))  # => "one"

# It maintains state as we iterate.
print("2.5.2", next(our_iterator))  # => "two"
print("2.5.3", next(our_iterator))  # => "three"

# After the iterator has returned all of its data, it raises a
# StopIteration exception
print("\n2.6 After the iterator has returned all of its data, it raises a \n\
StopIteration exception")
try:
    next(our_iterator)  # Raises StopIteration
except StopIteration as e:
    print("2.6.1 StopIteration error with next(our_iterator)")
else:
    print("2.6.1 No error with next(our_iterator)")

# We can also loop over it, in fact, "for" does this implicitly!
print("\n2.7 We can also loop over it, in fact, 'for' does this implicitly!")
print("2.7.1 for i in our_iterator: print(i)")
our_iterator = iter(our_iterable)
for i in our_iterator:
    print("2.7.1", i)  # Prints one, two, three

# You can grab all the elements of an iterable or iterator by call of list().
print("\n2.8 You can grab all the elements of an iterable/iterator with list().")

# Returns ["one", "two", "three"]
print("2.8.1 list(our_iterable) =>", list(our_iterable))

# Returns [] because state is saved
print("2.8.2 list(our_iterator) =>", list(our_iterator), "(note: saved state)")
