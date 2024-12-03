####################################################
##  Advanced Python Capabilities                  ##
####################################################
# This section demonstrates advanced Python features, focusing on:
# 1. Generators for efficient memory usage and lazy evaluation.
# 2. Generator comprehensions for concise and memory-efficient code.
# 3. Decorators for enhancing functions with additional behavior.
# 4. Using `functools.wraps` to preserve metadata in decorated functions.


####################################################
## 1. Generators
####################################################

print("\n1. Generators")
print("Generators are functions that allow lazy evaluation,")
print("yielding values one at a time as needed.")
print("They are memory-efficient and ideal for working with large datasets.")

print("\n1.1 Generator Example: for i in iterable")
def double_numbers(iterable):
    for i in iterable:
        yield i + i

# Generators load data only as needed, enabling operations on large datasets.
print("Code: for i in double_numbers(range(1, 9000)):")
# `range` itself is a generator in Python 3.
for i in double_numbers(range(1, 9000)):
    print("1.1." + str(int(i/2)) + " " + str(int(i/2)) + " =>", i)
    if i >= 30:
        break

# 1.2 Generator Comprehensions
# Similar to list comprehensions, but produce values lazily.
print("\n1.2 Generator Comprehensions:")

values = (-x for x in [1, 2, 3, 4, 5] if x < 5)
print("Code: for x in values:")
# Outputs: -1, -2, -3, -4
for x in values:
    print("1.2." + str(-x) + " " + str(-x) + " =>", x)

print("\n1.3 Generator Comprehensions (to list):")
# You can also convert a generator comprehension to a list.
values = (-x for x in [1, 2, 3, 4, 5] if x < 5)
print("Code: list(values):")
# => [-1, -2, -3, -4]
gen_to_list = list(values)
print("1.3.1 Converted to list:", gen_to_list)

####################################################
## 2. Decorators
####################################################

print("\n2. Decorators:")
print("Decorators allow you to modify or extend the behavior of functions.")
print("They simplify code by avoiding repetitive patterns.")

# Wrappers are one type of decorator.
# They're really useful for adding logging
# to existing functions without needing to modify them.

# 2.1 A simple logging decorator
print("\n2.1 Wrappers are one type of decorator, very useful for logging")
def log_function(func):
    def wrapper(*args, **kwargs):
        print("    Entering function:", func.__name__)
        result = func(*args, **kwargs)
        print("    Exiting function:", func.__name__)
        return result
    return wrapper

# Applying a decorator using @function_name
print("\n2.2 Apply decorator using @function_name")
@log_function           # equivalent:
def add_numbers(x, y):  # def add_numbers(x,y):
    return x + y        #   return x+y
                        # add_numbers = add_numbers(add_numbers)

# The decorator @log_function tells us as we begin reading the function
# definition for add_numbers that this function will be wrapped by log_function.
# When function definitions are long, it can be hard to parse the non-decorated
# assignment at the end of the definition.

# => "Entering function add_numbers"
# => "7"
# => "Exiting function add_numbers"
print("2.3 Demonstrate decorator functionality")
print("Code: add_numbers(3, 4):")
print("    Result:", add_numbers(3, 4))  # Outputs logs and result

# 2.4 Problem with Metadata in Decorators
# Decorators replace the original function with the wrapper function.
# This causes metadata like the function name or docstring to be lost.

print("\n2.4 Problem with Metadata in Decorators:")
print("Code: add_numbers.__name__:")
print("    Function name:", add_numbers.__name__) # => 'wrapper'
print("Code: add_numbers.__code__.co_argcount:")
print("    Argument count:", add_numbers.__code__.co_argcount) # => 0
# argcount is 0 because both arguments in wrapper()'s signature are optional.

# Because our decorator is equivalent to add_numbers = log_function(add_numbers)
# we've replaced information about add_numbers with information from wrapper

# Fix this using functools

####################################################
## 3. Fixing Metadata Loss with functools.wraps
####################################################

print("\n3. Fixing Metadata Loss with functools.wraps")
print("Using `functools.wraps` copies metadata")
print("from the original function to the wrapper.")

print("\n3.1 from functools import wraps")
from functools import wraps

print("3.1.1 apply using @wraps(func)")
# this ensures docstring, function name, arguments list, etc. are all copied
# to the wrapped function - instead of being replaced with wrapper's info
def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Entering function:", func.__name__)
        result = func(*args, **kwargs)
        print("Exiting function:", func.__name__)
        return result
    return wrapper

@log_function
def add_numbers(x, y):
    return x + y

# Demonstrate the fixed decorator
print("\n3.2 Fixing Metadata Loss with functools.wraps:")
print("Code: add_numbers(5, 6):")
print("    Result:", add_numbers(5, 6))  # Outputs logs and result
print("Code: add_numbers.__name__:")
print("    Function name:", add_numbers.__name__)  # => 'add_numbers'
print("Code: add_numbers.__code__.co_argcount:")
print("    Argument count:", add_numbers.__code__.co_argcount)  # => 2
