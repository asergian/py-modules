####################################################
##  Modules                                       ##
##  Importing and using external Python libraries ##
####################################################

print("\n5. Modules")
print("\nModules are Python's way of organizing and reusing code. ")
print("They allow you to import external libraries, use specific functions, ")
print("and manage code across different files and projects.")

# 5.1 Basic Module Importing
print("\n5.1 Basic Module Importing")
import math
print("5.1.1 import math")
print("5.1.2 math.sqrt(16) = ", math.sqrt(16))  # Shows code and result

# 5.2 Importing Specific Functions
print("\n5.2 Importing Specific Functions")
print("5.2.1 from math import ceil, floor")
from math import ceil, floor
print("5.2.2 ceil(3.7) = ", ceil(3.7))   # Shows code and result
print("5.2.3 floor(3.7) = ", floor(3.7))  # Shows code and result

# 5.3 Wildcard Import (Not Recommended)
print("\n5.3 Wildcard Import")
print("5.3.1 from math import * (imports all functions)")
from math import *

# 5.4 Module Aliasing
print("\n5.4 Module Aliasing")
print("5.4.1 import math as m")
import math as m
print("5.4.2 math.sqrt(16) = ", math.sqrt(16))
print("5.4.3 m.sqrt(16) = ", m.sqrt(16))
print("5.4.4 math.sqrt(16) == m.sqrt(16): ", math.sqrt(16) == m.sqrt(16))

# Python modules are just ordinary Python files. You
# can write your own, and import them. The name of the
# module is the same as the name of the file.

# You can find out which functions and attributes
# are defined in a module.

# 5.5 Listing Module Contents
print("\n5.5 Module Introspection")
print("5.5.1 dir(math)[:10] = ", dir(math)[:10])  # Shows first 10 module contents

# If you have a Python script named math.py in the same
# folder as your current script, the file math.py will
# be loaded instead of the built-in Python module.
# This happens because the local folder has priority
# over Python's built-in libraries.