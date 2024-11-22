##################################################
## 2. Variables and Collections                 ##
## Lists, Tuples, Dicts, Sets                   ##
##################################################

##################################################
# 4. Tuples

print("\n4. Tuples")
print("\n4.1 Tuple Basics")

# Tuples are like lists but are immutable.
tup = (1, 2, 3)
print("4.1.1 Define tup = (1,2,3)")
print("4.1.2 access element 1 tup[0] =", tup[0]) # => 1

# this will raise a TypeError
try:
    tup[0] = 3
except Exception as e:
    print("4.1.3 error when setting element tup[0] = 3")
    # raise e
else:
    print("4.1.3 no issue when setting tup[0] = 3!")

# Note that a tuple of length one has to have a comma after the last element but
# tuples of other lengths, even zero, do not.
print("\n4.2 Tuple Type")
print("4.2.1 access int element type(1) =", type((1)))   # => <class 'int'>

# both examples below are <class 'tuple'>
print("4.2.2 access element as tuple type((1,)) =", type((1,)))
print("4.2.3 empty tuple type(()) =",  type(()))

print("\n4.3 Tuple Operations")
# You can do most of the list operations on tuples too
print("4.3.1 len(tup) =", len(tup))         # => 3
tup2 = tup + (4, 5, 6)
print("4.3.2 tup composition tup + (4, 5, 6) =", tup2)  # => (1, 2, 3, 4, 5, 6)
print("4.3.3 tup slicing tup[:2] =", tup[:2])          # => (1, 2)
print("4.3.4 2 in tup =", 2 in tup)         # => True
print("4.3.5 4 in tup =", 4 in tup)         # => False

print("\n4.4 Tuple Unpacking")
# You can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
print(f"4.4.1 a, b, c = {a}, {b}, {c}")

# You can also do extended unpacking (SyntaxError with 2+ * vars)
a, *b, c = (1, 2, 3, 4)  # a is now 1, b is now [2, 3] and c is now 4
print(f"4.4.2 extended unpacking a, *b, c = (1, 2, 3, 4) => {a}, {b}, {c}")

# Tuples are created by default if you leave out the parentheses
d, e, f = 4, 5, 6  # tuple 4, 5, 6 is unpacked into variables d, e and f
print(f"4.4.3 d, e, f = {d}, {e}, {f}")

# respectively such that d = 4, e = 5 and f = 6
# Now look how easy it is to swap two values
e, d = d, e  # d is now 5 and e is now 4
print(f"4.4.4 swap values e, d = d, e: d = {d}, e = {e}")

##################################################
# 5. Dict

print("\n5. Dicts")
print("\n5.1 Dict Basics")

# Dictionaries store mappings from keys to values
empty_dict = {}
print(f"5.1.1 empty_dict = {empty_dict}")
# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}
print(f"5.1.2 filled_dict = {filled_dict}")

# Note keys for dictionaries have to be immutable types. This is to ensure that
# the key can be converted to a constant hash value for quick look-ups.
# Immutable types include ints, floats, strings, tuples.
try:
    # Yield a TypeError: unhashable type: 'list'
    invalid_dict = {[1,2,3]: "123"}
except TypeError as e:
    print("5.1.3 TypeError using mutable keys: {[1,2,3]: \"123\"}")
    # raise e
else:
    print("5.1.3 No problem using mutable keys: {[1,2,3]: \"123\"}!")

valid_dict = {(1,2,3):[1,2,3]}   # Values can be of any type, however.
print(f"5.1.4 No issue with mutable values: valid_dict = {valid_dict}")

print("\n5.2 Dict Access")

# Look up values with []
filled_dict["one"]  # => 1

# Get all keys as an iterable with "keys()". We need to wrap the call in list()
# to turn it into a list. We'll talk about those later.  Note - for Python
# versions <3.7, dictionary key ordering is not guaranteed. Your results might
# not match the example below exactly. However, as of Python 3.7, dictionary
# items maintain the order at which they are inserted into the dictionary.
list(filled_dict.keys())  # => ["three", "two", "one"] in Python <3.7
list(filled_dict.keys())  # => ["one", "two", "three"] in Python 3.7+


# Get all values as an iterable with "values()". Once again we need to wrap it
# in list() to get it out of the iterable. Note - Same as above regarding key
# ordering.
list(filled_dict.values())  # => [3, 2, 1]  in Python <3.7
list(filled_dict.values())  # => [1, 2, 3] in Python 3.7+

# Check for existence of keys in a dictionary with "in"
"one" in filled_dict  # => True
1 in filled_dict      # => False

# Looking up a non-existing key is a KeyError
filled_dict["four"]  # KeyError

# Use "get()" method to avoid the KeyError
filled_dict.get("one")      # => 1
filled_dict.get("four")     # => None
# The get method supports a default argument when the value is missing
filled_dict.get("one", 4)   # => 1
filled_dict.get("four", 4)  # => 4

# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5

# Adding to a dictionary
filled_dict.update({"four":4})  # => {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4         # another way to add to dict

# Remove keys from a dictionary with del
del filled_dict["one"]  # Removes the key "one" from filled dict

# From Python 3.5 you can also use the additional unpacking options
{"a": 1, **{"b": 2}}  # => {'a': 1, 'b': 2}
{"a": 1, **{"a": 2}}  # => {'a': 2}