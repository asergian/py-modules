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

print("##################################################")
print("1. Practice numericals and math operations")

# You have numbers
print("\n1.1 Numericals")
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
## 2. Booleans and comparisons
####################################################

print("\n##################################################")
print("2. Booleans and comparisons")

# Boolean values are primitives (Note: the capitalization)
print("\n2.1 Booleans, note True/False equate to 0/1")
print("2.1.1 True =", True)   # => True
print("2.1.2 False =", False)  # => False

# negate with not
print("\n2.2 Boolean Negation")
print("2.2.1 not True =", not True)   # => False
print("2.2.2 not False =", not False)  # => True

# Boolean Operators
# Note "and" and "or" are case-sensitive
print("\n2.3 Boolean Operations")
print("2.3.1 True and False =", True and False)  # => False
print("2.3.2 False or True =", False or True)   # => True

# True and False are actually 1 and 0 but with different keywords
print("2.3.3 True + True =", True + True)  # => 2
print("2.3.4 True * 8 =", True * 8)     # => 8
print("2.3.5 False - 5 =", False - 5)    # => -5

# Comparison operators look at the numerical value of True and False
print("2.3.6 0 == False:", 0 == False)   # => True
print("2.3.7 2 > True:", 2 > True)     # => True
print("2.3.8 2 == True:", 2 == True)    # => False
print("2.3.9 -5 != False:", -5 != False)  # => True

# None, 0, and empty strings/lists/dicts/tuples/sets all evaluate to False.
# All other values are True
print("\n2.4 Boolean Evaluations using bool(); empty objs equate to False")
print("2.4.1 bool(0) =", bool(0))      # => False
print("2.4.2 book('') =", bool(""))     # => False
print("2.4.3 bool([]) =", bool([]))     # => False
print("2.4.4 bool({}) =", bool({}))     # => False
print("2.4.5 bool(()) =", bool(()))     # => False
print("2.4.6 bool(set()) =", bool(set()))  # => False
print("2.4.7 bool(4) =", bool(4))      # => True
print("2.4.8 bool(-6) =", bool(-6))     # => True
print("2.4.9 bool() =", bool())     # => False

print("\n2.5 Boolean evaluations with casted numericals")
# Using boolean logical operators on ints casts them to booleans for evaluation,
# but their non-cast value is returned. Don't mix up with bool(ints) and bitwise
# and/or (&,|)
print("2.5.1 bool(0) =", bool(0))   # => False
print("2.5.2 bool(2) =", bool(2))   # => True
print("2.5.3 0 and 2 =", 0 and 2)   # => 0
print("2.5.4 3 and 2 =", 3 and 2)   # => 2
print("2.5.5 bool(-5) =", bool(-5))  # => True
print("2.5.6 bool(2) =", bool(2))   # => True
print("2.5.7 -5 or 0 =", -5 or 0)   # => -5
print("2.5.8 -5 or 1 =", -5 or 1)   # => -5
print("2.5.9 1 or -5 =", 1 or -5)   # => 1

print("\n2.6 Operators with Numericals")
# Equality is ==
print("2.6.1 1 == 1:", 1 == 1)  # => True
print("2.6.2 2 == 1:", 2 == 1)  # => False

# Inequality is !=
print("2.6.3 1 != 1:", 1 != 1)  # => False
print("2.6.4 2 != 1:", 2 != 1) # => True

# More comparisons
print("2.6.5 1 < 10:", 1 < 10)  # => True
print("2.6.6 1 > 10:", 1 > 10)  # => False
print("2.6.7 2 <= 2:", 2 <= 2)  # => True
print("2.6.8 2 >= 2:", 2 >= 2)  # => True

# Seeing whether a value is in a range
print("\n2.7 Chained Boolean Operators")
print("2.7.1 1 < 2 and 2 < 3:", 1 < 2 and 2 < 3)  # => True
print("2.7.2 2 < 3 and 3 < 2:", 2 < 3 and 3 < 2)  # => False
# Chaining makes this look nicer
print("2.7.3 1 < 2 < 3:", 1 < 2 < 3)  # => True
print("2.7.4 2 < 3 < 2:", 2 < 3 < 2)  # => False

# (is vs. ==) is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values.
print("\n2.8 Comparison with 'is' operator")
a = [1, 2, 3, 4]
print("2.8.1 Declare a = [1, 2, 3, 4]")  # Point a at a new list, [1, 2, 3, 4]
b = a
print("2.8.2 Point b to object a: b = a") # Point b at what a is pointing to
print("2.8.3 b is a:", b is a)  # => True, a and b refer to the same object
print("2.8.4 b == a:", b == a)  # => True, a's and b's objects are equal
b = [1, 2, 3, 4]
# Point b at a new list, [1, 2, 3, 4]
print("2.8.5 Declare b = [1, 2, 3, 4] (distinct list from a)")
# => False, a and b do not refer to the same object
print("2.8.6 b is a:", b is a)
# => True, a's and b's objects are equal
print("2.8.7 b == a:", b == a)

####################################################
## 3. Strings
####################################################

print("\n##################################################")
print("3. Strings")

# Strings are created with " or '
print("3.1 String Basics")
print("3.1.1 \"This is a string.\" =", "This is a string.")
print("3.1.2 'This is also a string.' =", 'This is also a string.')

# Strings can be added too
print("3.1.3 \"Hello\" + \"world!\" =", "Hello " + "world!") # => "Hello world!"
# String literals (but not variables) can be concatenated without using '+'
print("3.1.4 \"Hello \" \"world!\" =", "Hello " "world!")    # => "Hello world!"

# A string can be treated like a list of characters
print("3.1.5 \"Hello world!\"[0] =", "Hello world!"[0])  # => 'H'

# You can find the length of a string
print("3.1.6 len(\"This is a string\") =", len("This is a string"))  # => 16

print("\n3.2 f-strings")
# Since Python 3.6, you can use f-strings or formatted string literals.
name = "Reiko"
print("3.2.1 Set name =", name)
print("3.2.2 f\"She said her name is {name}.\" =",
      f"She said her name is {name}.")  # => "She said her name is Reiko"
# Any valid Python expression inside these braces is returned to the string.

# => "Reiko is 5 characters long."
print("3.2.2 f\"{name} is {len(name)} characters long.\" =",
      f"{name} is {len(name)} characters long.")

print("\n3.3 None as object")
# None is an object
print("3.3.1 None =", None)  # => None

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead. This checks for equality of object identity.
print("3.3.2 \"etc\" is None =", "etc" is None)  # => False)
print("3.3.3 None is None =", None is None)   # => True