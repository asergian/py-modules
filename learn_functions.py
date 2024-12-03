####################################################
##  Functions                                     ##
## Covers: Function Definitions, Args, Scope,     ##
## Closures, Lambda Functions,                    ##
## Higher-Order Functions, List Comprehensions    ##
####################################################

####################################################
## 1. Function definition and args
####################################################

print("1. Function definition and args")

# Use "def" to create new functions
print("\n1.1 Use 'def fname(args):' to create new functions")
print("1.1 def add(x,y): return x+y")
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y  # Return values with a return statement

print("\n1.3 Calling functions with parameters")
# => prints out "x is 5 and y is 6" and returns 11
print("1.3 add(5, 6) =>", add(5, 6))

print("\n1.4 Another way to call functions is with keyword arguments")
# Keyword arguments can arrive in any order.
print("1.4 add(y=6, x=5) =>", add(y=6, x=5))

print("\n1.5 Functions can take a variable number of positional arguments")
print("1.5.1 def varargs(*args)")

# You can define functions that take a variable number of
# positional arguments
def varargs(*args):
    return args

print("1.5.2 varargs(1, 2, 3) =>", varargs(1, 2, 3))  # => (1, 2, 3)

print("\n1.6 Functions can take a variable number of keyword arguments as well")
print("1.6.1 def keyword_args(**kwargs)")

# You can define functions that take a variable number of
# keyword arguments, as well
def keyword_args(**kwargs):
    return kwargs

print('1.6.2 keyword_args(big="foot", loch="ness") =>', \
keyword_args(big="foot", loch="ness"))  # => {"big": "foot", "loch": "ness"}

print("\n1.7 You can do both at once, if you like")
print("1.7.1 def all_the_args(*args, **kwargs)")

def all_the_args(*args, **kwargs):
    print(f"\t{args}")
    print(f"\t{kwargs}")
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""

print("1.7.2 all_the_args(1, 2, a=3, b=4) =>", all_the_args(1, 2, a=3, b=4))

print("\n1.8 complex examples with: def concatenate(a, *args, **kwargs)")
print("1.8 note: dictionaries need to be unpacked to serve as kwargs")

def concatenate(a, *args, **kwargs):
    print(f"\ta: {a}")
    print(f"\targs: {args}")
    print(f"\tkwargs: {kwargs}")

    result = "Concat: " + a

    # Iterating over the keys of the Python kwargs dictionary
    for arg in args:
        result += str(arg)

    # Iterating over the keys of the Python kwargs dictionary
    for arg in kwargs.values():
        result += str(arg)
    return result

print('\n1.8.1 pass keyword args using \
concatenate(a="Real", b="Python", c="Is", d="Great", e="!")')
print('1.8.1', concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

a="A"
b="B"
c="C"
print(f"\n1.8.2 a = {a}, b= {b}, c = {c}")
print(f"1.8.2 pass positional args using concatenate(a, b, c)")
print(concatenate(a, b, c))

dict_args = {a:"Real", b:"Python", c:"Is"}
print(f'\n1.8.3 dict_args = {dict_args}')
print(f'1.8.3 concatenate(a, b, dict_args, b="c")')
print(concatenate(a, b, dict_args, b="c"))

print('\n1.8.4 unpack keys using concatenate(a, *dict_args, b="c")')
print(concatenate(a, *dict_args, b="c"))

dict_args = {'e':"Real", b:"Python", 'c':"Is"}
print(f'\n1.8.5 dict = {dict_args}')
print(f'1.8.5 unpack values using concatenate(a, b, **dict_args, b="c")')
print(concatenate(a, b, **dict_args, b="c"))

print("\n1.9 When calling functions, you can do the opposite of args/kwargs!")
print("Use * to expand args (tuples) and use ** to expand kwargs (dicts).")
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
print(f"1.9 args = {args}, kwargs = {kwargs}")

# equivalent: all_the_args(1, 2, 3, 4)
print("\n1.9.1 all_the_args(*args) <==> all_the_args(1, 2, 3, 4)")
all_the_args(*args)

# equivalent: all_the_args(a=3, b=4)
print("\n1.9.2 all_the_args(a=3, b=4) <==> all_the_args(**kwargs)")
all_the_args(**kwargs)

# equivalent: all_the_args(1, 2, 3, 4, a=3, b=4)
print("\n1.9.3 all_the_args(1, 2, 3, 4, a=3, b=4) <==> \
all_the_args(*args, **kwargs)")
all_the_args(*args, **kwargs)


####################################################
## Functions: Advanced Python Function Techniques ##
## Covers: Function Definitions, Scope, Closures, ##
## Lambda Functions, Higher-Order Functions,      ##
## Comprehensions                                 ##
####################################################

####################################################
## 2. Basic Function Definitions and Return Values
####################################################
print("\n2. Basic Function Definitions and Return Values\n")

# 2.1 Simple Function Definition
def greet(name):
    return f"Hello, {name}!"

print("2.1 Basic function call: greet('Python Learner') =", 
    greet("Python Learner"))

# 2.2 Returning Multiple Values
def swap(x, y):
    # Demonstrate returning multiple values as a tuple
    print("2.2.2 Function: swap(x, y) called with x =", x, ", y =", y)
    return y, x  # Implicit tuple return

x, y = 1, 2
print("2.2.1 Before swap: x =", x, ", y =", y)
x, y = swap(x, y)
print("2.2.3 After swap(x, y): x =", x, ", y =", y)

# 2.3 Default Arguments
print("2.3 Default Arguments")
def power(base, exponent=2):
    print(f"2.3.2 Calculating {base} raised to power {exponent}")
    return base ** exponent

print("2.3.1 Default exponent (squared): power(4) =", power(4))
print("2.3.3 Custom exponent: power(4, 3) =", power(4, 3))

# 2.4 Variable Number of Arguments
def sum_all(*args):
    print("2.4 Summing arguments sum(args):", args)
    return sum(args)

print("2.4.1 Sum of multiple arguments: sum_all(1, 2, 3, 4) =", 
    sum_all(1, 2, 3, 4))
print("2.4.2 Sum of different number of arguments: sum_all(10, 20) =", 
    sum_all(10, 20))

####################################################
## 3. Function Scope and Global Variables
####################################################
print("\n3. Function Scope and Global Variables\n")

# Global variable
x = 5
print("3.1 Initial global x:", x)

def modify_local_x(num):
    # Demonstrate local variable scope
    print("3.2 Attempting to modify local x. Code: x = num (with num =", 
        num, ")")
    x = num  # Local variable, doesn't affect global x
    print("3.3 Local x inside function:", x)

def modify_global_x(num):
    # Demonstrate global variable modification
    global x
    print("3.4 Global x before modification:", x)
    print("3.5 Modifying global x. Code: x = num (with num =", num, ")")
    x = num
    print("3.6 Global x after modification:", x)

modify_local_x(10)
print("3.7 Global x after local modification:", x)

modify_global_x(15)
print("3.8 Global x after global modification:", x)

####################################################
## 4. Closures and Nested Functions
####################################################
print("\n4. Closures and Nested Functions\n")

print("4.1 Create a closure that multiplies by 2: \
double = create_multiplier(2)")

def create_multiplier(factor):
    # Demonstrate closure by creating a function that multiplies by a factor
    print("4.2 Creating multiplier with factor =", factor)
    def multiplier(x):
        print(f"4.3 Multiplying {x} * {factor}")
        return x * factor
    return multiplier

# Create a closure that multiplies by 2
double = create_multiplier(2)
print("4.4 Calling double(5):", double(5))  # => 10

# Closures in nested functions:
# We can use the nonlocal keyword to work with variables in nested scope 
# which shouldn't be declared in the inner functions.
print("4.5 use nonlocal keyword to work with vars outside nested scope")
def create_counter():
    print("4.6 create_counter() function defined: Creates a nested function \
that maintains a persistent count")
    count = 0
    def counter():
        print("\tInner counter() function: Increments and returns the \
persistent count")
        nonlocal count
        count += 1
        return count
    return counter

# Demonstrating a closure-based counter
my_counter = create_counter()
print("4.6.1 my_counter = create_counter()")
print("4.6.2 First call: counter.count starts at 0, increments to 1, returns:", 
    my_counter())
print("4.6.3 Second call: counter.count was 1, increments to 2, returns:", 
    my_counter())
print("4.6.4 Third call: counter.count was 2, increments to 3, returns:", 
    my_counter())

####################################################
## 5. Lambda Functions and Higher-Order Functions
####################################################
print("\n5. Lambda Functions and Higher-Order Functions\n")

# 5.1 Simple Lambda Function
print("5.1 Lambda to check if number > 2: (lambda x: x > 2)(3) =", 
       (lambda x: x > 2)(3))

# 5.2 Lambda with multiple arguments
print("5.2 Lambda square sum: (lambda x, y: x**2 + y**2)(2, 1) =", 
       (lambda x, y: x**2 + y**2)(2, 1))

# 5.3 Map Function
def add_ten(x):
    return x + 10

numbers = [1, 2, 3]
print("5.3 Map with add_ten: list(map(add_ten, [1, 2, 3])) =", 
       list(map(add_ten, numbers)))

# 5.4 Filter Function
print("5.4 Filter numbers > 5: list(filter(lambda x: x > 5, \
[3, 4, 5, 6, 7])) =", list(filter(lambda x: x > 5, [3, 4, 5, 6, 7])))

####################################################
## 6. List, Set, and Dict Comprehensions
####################################################
print("\n6. List, Set, and Dict Comprehensions\n")

# 6.1 List Comprehension
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print("6.1 List comprehension - squared numbers: [x**2 for x in [1,2,3,4,5]] =", 
       squared)

# 6.2 Filtered List Comprehension
even_squared = [x**2 for x in numbers if x % 2 == 0]
print("6.2 Filtered list comprehension - even squared: [x**2 for x in \
[1,2,3,4,5] if x % 2 == 0] =", even_squared)

# 6.3 Set Comprehension
unique_chars = {x for x in "abcddeef" if x not in "abc"}
print("6.3 Set comprehension - unique chars: {x for x in 'abcddeef' \
if x not in 'abc'} =", unique_chars)

# 6.4 Dictionary Comprehension
squared_dict = {x: x**2 for x in range(5)}
print("6.4 Dict comprehension - squared dict: {x: x**2 for x in range(5)} =", 
       squared_dict)