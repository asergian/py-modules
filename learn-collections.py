####################################################
##  Collections                                   ##
##  Basics of Lists, Tuples, Dicts, Sets          ##
####################################################

####################################################
## 1. Practice List creation, append, pop
####################################################

print("\n1. Practice list creation, append, pop\n")

# Creating a List with 
# the use of multiple values 
List = ["Geeks", "For", "Geeks"] 
print("1.0 Empty list:", [])
print("1.1.1 List containing multiple values:", List)

# Creating a Multi-Dimensional List 
# (By Nesting a list inside a List) 
List2 = [['Geeks', 'For'], ['Geeks']] 
print("1.2. Multi-Dimensional List:", List2) 

# accessing a element from the  
# list using index number 
print("1.3 Accessing element from the list. #0:", List[0], ", #1:", List[2]) 

# accessing a element using 
# negative indexing 
print("1.4 Accessing element using negative indexing")

# print the last element of list 
print("1.4.1 Last element of the list:", List[-1])
    
# print the third last element of list  
print("1.4.2 Third to last element of the list:", List[-3]) 

# list with multiple data types
List3 = [1, 2,  3, "GFG", 2.3]
print("1.5 List with multiple data types:", List3)

# add element to end of list using List.append(value)
List3.append(5)
List3.append("ok")
print("1.6 Append elements 5 and 'ok' to list:", List3)

# remove element from end of list using List.pop()
x = List3.pop() # remove the last element and store it in x
List3.append(x) # put the last element back
print("1.7 Pop then reappend value to list. Value:", x, ", List:", List3)

try:
    print(List3[7]) # raises IndexError
except IndexError as e:
    print("1.8 IndexError when accesing List3[7]")
else:
    print("1.8 No issue when accesing List3[7]")

####################################################
## 2. Practice list splicing, indexing, removing
####################################################
print("\n2. Practice list splicing, indexing, removal\n")
li = [1, 2, 4, 3]
print("2.0 li =", li)

# You can look at ranges with slice syntax.
# The start index is included, the end index is not
# (It's a closed/open range for you mathy types.)
print('2.1 li[1:3] =', li[1:3]) # Return list from index 1 to 3 => [2, 4]
print('2.2 li[2:] =', li[2:]) # Return list starting from index 2 => [4, 3]
print('2.3 li[:3] =', li[:3]) # Return beginning until index 3 => [1, 2, 4]
print('2.4 li[::2] =', li[::2]) # Get elements with a step size of 2 => [1, 4]
print('2.5 li[::-1] =',li[::-1]) # Return list in reverse order => [3, 4, 2, 1]
# Use any combination of these to make advanced slices
# li[start:end:step]

# Make a one layer deep copy using slices
li2 = li[:]  # => li2 = [1, 2, 4, 3] but (li2 is li) will result in false.

# Remove arbitrary elements from a list with "del"
del li[2]  # li is now [1, 2, 3]
print("2.6 Remove index 2 using 'del li[2]'", li)

# Remove first occurrence of a value
li.remove(2)  # li is now [1, 3]
print("2.7 Removed first occurance of '2' using li.remove(2):'", li)

try:
    li.remove(2)  # Raises a ValueError as 2 is not in the list
except ValueError as e:
    print("2.7.1 ValueError when attempting li.remove(2)")
else:
    print("2.7.1 No issues when attempting li.remove(2)")

# Insert an element at a specific index
li.insert(1, 2)  # li is now [1, 2, 3] again
print("2.8 Reinsert 2 and index 1 using 'li.insert(1, 2)'", li)

# Get the index of the first item found matching the argument
print("2.9 Get index of first '2' using li.index(2)", li.index(2)) # => 1

try:
    li.index(4)  # Raises a ValueError as 4 is not in the list
except ValueError as e:
    print("2.9.1 ValueError when attempting li.index(4)")
else:
    print("2.9.1 No issues when attempting li.index(4)")

# You can add lists
# Note: values for li and for other_li are not modified.
other_li = [4, 5, 6]
li + other_li  # => [1, 2, 3, 4, 5, 6]
print("2.10 List addition. other_li =", other_li)
print("2.10.1 li + other_li =", li + other_li)

# Concatenate lists with "extend()"
# Note: values for li are modified
li.extend(other_li)  # Now li is [1, 2, 3, 4, 5, 6]
print("2.10.2 li.extend(other_li) =", li)

# Check for existence in a list with "in"
print("2.11 Check for existence in a list with 'in'", 1 in li)  # => True

# Examine the length with "len()"
print("2.12 len(li)", len(li))  # => 6

####################################################
## 3. Tuples
####################################################

print("\n4. Tuples")
print("\n4.1 Tuple Basics")

# Tuples are like lists but are immutable.
tup = (1, 2, 3)
print("3.1.1 Define tup = (1,2,3)")
print("3.1.2 access element 1 tup[0] =", tup[0]) # => 1

# this will raise a TypeError
try:
    tup[0] = 3
except Exception as e:
    print("3.1.3 error when setting element tup[0] = 3")
    # raise e
else:
    print("3.1.3 no issue when setting tup[0] = 3!")

# Note that a tuple of length one has to have a comma after the last element but
# tuples of other lengths, even zero, do not.
print("\n4.2 Tuple Type")
print("3.2.1 access int element type(1) =", type((1)))   # => <class 'int'>

# both examples below are <class 'tuple'>
print("3.2.2 access element as tuple type((1,)) =", type((1,)))
print("3.2.3 empty tuple type(()) =",  type(()))

print("\n4.3 Tuple Operations")
# You can do most of the list operations on tuples too
print("3.3.1 len(tup) =", len(tup))         # => 3
tup2 = tup + (4, 5, 6)
print("3.3.2 tup composition tup + (4, 5, 6) =", tup2)  # => (1, 2, 3, 4, 5, 6)
print("3.3.3 tup slicing tup[:2] =", tup[:2])          # => (1, 2)
print("3.3.4 2 in tup =", 2 in tup)         # => True
print("3.3.5 4 in tup =", 4 in tup)         # => False

print("\n4.4 Tuple Unpacking")
# You can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
print(f"3.4.1 a, b, c = {a}, {b}, {c}")

# You can also do extended unpacking (SyntaxError with 2+ * vars)
a, *b, c = (1, 2, 3, 4)  # a is now 1, b is now [2, 3] and c is now 4
print(f"3.4.2 extended unpacking a, *b, c = (1, 2, 3, 4) => {a}, {b}, {c}")

# Tuples are created by default if you leave out the parentheses
d, e, f = 4, 5, 6  # tuple 4, 5, 6 is unpacked into variables d, e and f
print(f"3.4.3 d, e, f = {d}, {e}, {f}")

# respectively such that d = 4, e = 5 and f = 6
# Now look how easy it is to swap two values
e, d = d, e  # d is now 5 and e is now 4
print(f"3.4.4 swap values e, d = d, e: d = {d}, e = {e}")

####################################################
## 4. Dict
####################################################

print("\n4. Dicts")
print("\n4.1 Dict Basics")

# Dictionaries store mappings from keys to values
empty_dict = {}
print(f"4.1.1 empty_dict = {empty_dict}")
# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}
print(f"4.1.2 filled_dict = {filled_dict}")

# Note keys for dictionaries have to be immutable types. This is to ensure that
# the key can be converted to a constant hash value for quick look-ups.
# Immutable types include ints, floats, strings, tuples.
try:
    # Yield a TypeError: unhashable type: 'list'
    invalid_dict = {[1,2,3]: "123"}
except TypeError as e:
    print("4.1.3 TypeError using mutable keys: {[1,2,3]: \"123\"}")
    # raise e
else:
    print("4.1.3 No problem using mutable keys: {[1,2,3]: \"123\"}!")

valid_dict = {(1,2,3):[1,2,3]}   # Values can be of any type, however.
print(f"4.1.4 No issue with mutable values: valid_dict = {valid_dict}")

print("\n4.2 Dict Access")

# Look up values with []
print(f"4.2.1 Get element: filled_dict[\"one\"] = {filled_dict["one"]}") # => 1

# Get all keys as an iterable with "keys()". We need to wrap the call in list()
# to turn it into a list. We'll talk about those later.  Note - for Python
# versions <3.7, dictionary key ordering is not guaranteed. Your results might
# not match the example below exactly. However, as of Python 3.7, dictionary
# items maintain the order at which they are inserted into the dictionary.
# list(filled_dict.keys())  # => ["three", "two", "one"] in Python <3.7
print(f"4.2.2 filled_dict.keys() = {filled_dict.keys()}")
# Returns ["one", "two", "three"] in Python 3.7+
print(f"4.2.3 list(filled_dict.keys()) = {list(filled_dict.keys())}") 

# Get all values as an iterable with "values()". Once again we need to wrap it
# in list() to get it out of the iterable. Note - Same as above regarding key
# ordering.
# list(filled_dict.values())  # => [3, 2, 1]  in Python <3.7
# list(filled_dict.values())  # => [1, 2, 3] in Python 3.7+
print(f"4.2.4 filled_dict.values() = {filled_dict.values()}")
print(f"4.2.5 list(filled_dict.values()) = {list(filled_dict.values())}")

# Check for existence of keys in a dictionary with "in"
print(f"4.2.6 \"one\" in filled_dict = {"one" in filled_dict}")  # => True
print(f"4.2.7 1 in filled_dict = {1 in filled_dict}")      # => False

# Looking up a non-existing key is a KeyError
try:
    filled_dict["four"]  # KeyError
except KeyError as e:
    print("4.2.8 KeyError accessing filled_dict['four']")
    # raise e
else:
    print("4.2.8 No issues accessing filled_dict['four']")

print("\n4.3 Get Command")
# Use "get()" method to avoid the KeyError
print(f"4.3.1 filled_dict.get('one') = {filled_dict.get("one")}") # => 1
print(f"4.3.2 filled_dict.get('four') = {filled_dict.get("four")}") # => None
# The get method supports a default argument when the value is missing
print(f"4.3.3 filled_dict.get('one', 4) = {filled_dict.get("one", 4)}") # => 1
print(f"4.3.4 filled_dict.get('four', 4) = {filled_dict.get("four", 4)}") # => 4

print("\n4.4 Update Dict")
# "setdefault()" inserts into a dictionary only if the given key isn't present
print(f"4.4.1 filled_dict.setdefault('five', 5) = \
    {filled_dict.setdefault("five", 5)}")  # filled_dict["five"] is set to 5
print(f"4.4.2 filled_dict.setdefault('five', 6) = \
    {filled_dict.setdefault("five", 6)}")  # filled_dict["five"] is still 5

# Adding to a dictionary
# Update dict to {"one": 1, "two": 2, "three": 3, "five": 5, "four": 4}
filled_dict.update({"four":4})
print("4.4.3 filled_dict.update({'four':4}) =>", filled_dict)
filled_dict['four'] = 4 # another way to add to dict
print("4.4.4 filled_dict.filled_dict['four'] = 4", filled_dict)

# Remove keys from a dictionary with del
del filled_dict["one"] # Removes the key "one" from filled dict
print("4.4.5 del filled_dict['one']: ", filled_dict)

# From Python 3.5 you can also use the additional unpacking options
print("\n4.5 Unpack Dict")
print('4.5.1 {"a": 1, **{"b": 2}} =', {"a": 1, **{"b": 2}}) # => {'a':1, 'b':2}
print('4.5.2 {"a": 1, **{"a": 2}} =', {"a": 1, **{"a": 2}})  # => {'a':2}
print('4.5.3 {"a": 1, "a": 2} =', {"a": 1, "a": 2})  # => {'a':2}

person = {'name': 'John', 'age': 30, 'city': 'New York'}
print(f"4.5.4 person = {person}")
print("4.5.5 *person = ", *person)
print("4.5.6 *person.values() = ", *person.values())
print("4.5.7 *person.items() = ", *person.items())

# Merge dicts
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'd': 4} # updated b value 3 will be take precedence on merge
merged_dict = {**dict1, **dict2} # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("4.5.8 merge {**dict1, **dict2} =", merged_dict)

####################################################
## 5. Sets
####################################################

print("\n5. Sets")
print("\n5.1 Set Basics")

# Sets store ... well sets
empty_set = set()
print(f"5.1.1 empty_set = {empty_set}")

# Initialize a set with a bunch of values.
some_set = {1, 1, 2, 2, 3, 4}  # some_set is now {1, 2, 3, 4}
print("5.1.2 some_set = {1, 1, 2, 2, 3, 4} =>", some_set)

# Similar to keys of a dictionary, elements of a set have to be immutable.
try:
    invalid_set = {[1], 1}  # => Raises a TypeError: unhashable type: 'list'
except TypeError as e:
    print(f"5.1.3 TypeError with mutable element: {[1], 1}")
    # raise e
else:
    print(f"5.1.3 No issues with mutable key: {[1], 1}")

valid_set = {(1,), 1}
print(f"5.1.4 Tuples are valid elements: {valid_set}")

# Add one more item to the set
filled_set = some_set
filled_set.add(5)  # filled_set is now {1, 2, 3, 4, 5}
print(f"5.1.5 filled_set.add(5): {filled_set}")

# Sets do not have duplicate elements
filled_set.add(5)  # it remains as before {1, 2, 3, 4, 5}
print(f"5.1.6 Adding 5 leaves set unchanged (no dups allowed): {filled_set}")

print("\n5.2 Set operations")

# Do set intersection with &
other_set = {3, 4, 5, 6}
print(f"5.2.1 other_set = {other_set}")
print(f"5.2.2 filled_set & other_set = {filled_set & other_set}") # => {3, 4, 5}

# Do set union with |
# Returns {1, 2, 3, 4, 5, 6}
print(f"5.2.3 filled_set | other_set = {filled_set | other_set}")

# Do set difference with -
print("5.2.4 {1, 2, 3, 4} - {2, 3, 5} =", {1, 2, 3, 4} - {2, 3, 5}) # => {1, 4}

# Do set symmetric difference with ^
print("5.2.5 {1, 2, 3, 4} ^ {2, 3, 5} =", {1, 2, 3, 4} ^ {2, 3, 5}) # => {1,4,5}

# Check if set on the left is a superset of set on the right
print("5.2.6 {1, 2} >= {1, 2, 3} =", {1, 2} >= {1, 2, 3}) # => False

# Check if set on the left is a subset of set on the right
{1, 2} <= {1, 2, 3}  # => True
print("5.2.7 {1, 2} <= {1, 2, 3} =", {1, 2} <= {1, 2, 3}) # => True
print("5.2.8 {1, 2, 3} < {1, 2, 3} =", {1, 2, 3} < {1, 2, 3}) # => False

print("\n5.3 in/is operators")

# Check for existence in a set with in
print("5.3.1 2 in filled_set =", 2 in filled_set)   # => True
print("5.3.2 10 in filled_set =", 10 in filled_set)  # => False

# Make a one layer deep copy
filled_set = some_set.copy()  # filled_set is {1, 2, 3, 4, 5}
print(f"5.3.3 filled_set = some_set.copy() => {filled_set}")
print(f"5.3.4 filled_set is some_set => {filled_set is some_set}") # => False