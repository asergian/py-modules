####################################################
##    Primitive Datatypes and Operators           ##
##    Basics of numericals, math operations,      ##
##    booleans, comparisons, strings, and None    ##
####################################################

## 1. Comments

# Single line comments start with a number symbol.

""" Multiline strings can be written
    using three "s, and are often used
    as documentation.
"""

####################################################
## 1. Numericals and math operations
####################################################

print("\n1. Practice numericals and math operations\n")

# You have numbers
print("1.1 Numericals")
print("1.1.1 Interger: ", 3)  # => 3
print("1.1.2 Decimal: ", 3.0)  # => 3.0

# Math is what you would expect
print("\n1.2 Basic math is what you would expect")
print("1.2.1 Add 1 + 1 =", 1 + 1)   # => 2
print("1.2.2 Subtract 8 - 1 =", 8 - 1)   # => 7
print("1.2.3 Multiple 10 * 2 =", 10 * 2)  # => 20
print("1.2.4 Divide 35 / 5 =", 35 / 5)  # => 7.0
# The result of division is always a float. Below yields 3.33333
print("1.2.5 The result of division is always a float, 10.0 / 3 =", 10.0 / 3)
print("1.2.6 Divide 35 / 6:", 35 / 6)  # => 5.83333, repeating
print("1.2.7 Round to 2 places, round(35/6, 2) =", round(35 / 6, 2))  # => 5.83

# Floor division rounds towards negative infinity
print("\n1.3 Floor division rounds towards negative infinity")
print("1.3.2 Divide 5 // 3 =", 5 // 3)       # => 1
print("1.3.3 Divide -5 // 3 =", -5 // 3)      # => -2
print("1.3.4 Divide 5 // -3 =", 5 // -3)      # => -2
print("1.3.5 Divide -5 // -3 =", -5 // -3)      # => 1
print("1.3.6 Divide 5.0 // 3 =", 5.0 // 3)   # => 1.0  # works on floats too
print("1.3.7 Divide -5.0 // 3.0 =", -5.0 // 3.0)  # => -2.0

print("\n1.4 Modulo: remainder after //. Note: i % j share sign of j, unlike C")
# Modulo operation
print("1.4.1 5 % 3 =", 5 % 3)   # => 2
# i % j have the same sign as j, unlike C
print("1.4.2 -5 % 3 =", -5 % 3)  # => 1
print("1.4.3 5 % -3 =", 5 % -3)  # => -1
print("1.4.4 -5 % -3 =", -5 % -3)  # => -2

# Exponentiation (x**y, x to the yth power)
print("\n1.5 Exponentiation (x**y, x to the yth power)")
print("1.5.1 2**3 =", 2**3)  # => 8
print("1.5.2 -2**3 =", -2**3)  # => -8
print("1.5.3 2**-3 =", 2**-3)  # => 0.125
print("1.5.4 -2**-3 =", -2**-3)  # => -0.125

# Enforce precedence with parentheses
print("\n1.6 Enforce precedence with parentheses")
print("1.6.1 1 + 3 * 2 =", 1 + 3 * 2)    # => 7
print("1.6.2 (1 + 3) * 2 =", (1 + 3) * 2)  # => 8

####################################################
## 1. Booleans and comparisons
####################################################

# Boolean values are primitives (Note: the capitalization)
True   # => True
False  # => False

# negate with not
not True   # => False
not False  # => True

# Boolean Operators
# Note "and" and "or" are case-sensitive
True and False  # => False
False or True   # => True

# True and False are actually 1 and 0 but with different keywords
True + True  # => 2
True * 8     # => 8
False - 5    # => -5

# Comparison operators look at the numerical value of True and False
0 == False   # => True
2 > True     # => True
2 == True    # => False
-5 != False  # => True

# None, 0, and empty strings/lists/dicts/tuples/sets all evaluate to False.
# All other values are True
bool(0)      # => False
bool("")     # => False
bool([])     # => False
bool({})     # => False
bool(())     # => False
bool(set())  # => False
bool(4)      # => True
bool(-6)     # => True

# Using boolean logical operators on ints casts them to booleans for evaluation,
# but their non-cast value is returned. Don't mix up with bool(ints) and bitwise
# and/or (&,|)
bool(0)   # => False
bool(2)   # => True
0 and 2   # => 0
bool(-5)  # => True
bool(2)   # => True
-5 or 0   # => -5

# Equality is ==
1 == 1  # => True
2 == 1  # => False

# Inequality is !=
1 != 1  # => False
2 != 1  # => True

# More comparisons
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Seeing whether a value is in a range
1 < 2 and 2 < 3  # => True
2 < 3 and 3 < 2  # => False
# Chaining makes this look nicer
1 < 2 < 3  # => True
2 < 3 < 2  # => False

# (is vs. ==) is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values.
a = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]
b = a             # Point b at what a is pointing to
b is a            # => True, a and b refer to the same object
b == a            # => True, a's and b's objects are equal
b = [1, 2, 3, 4]  # Point b at a new list, [1, 2, 3, 4]
b is a            # => False, a and b do not refer to the same object
b == a            # => True, a's and b's objects are equal

# Strings are created with " or '
"This is a string."
'This is also a string.'

# Strings can be added too
"Hello " + "world!"  # => "Hello world!"
# String literals (but not variables) can be concatenated without using '+'
"Hello " "world!"    # => "Hello world!"

# A string can be treated like a list of characters
"Hello world!"[0]  # => 'H'

# You can find the length of a string
len("This is a string")  # => 16

# Since Python 3.6, you can use f-strings or formatted string literals.
name = "Reiko"
f"She said her name is {name}."  # => "She said her name is Reiko"
# Any valid Python expression inside these braces is returned to the string.
f"{name} is {len(name)} characters long."  # => "Reiko is 5 characters long."

# None is an object
None  # => None

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead. This checks for equality of object identity.
"etc" is None  # => False
None is None   # => True