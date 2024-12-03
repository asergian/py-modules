####################################################
##  Classes                                       ##
##  Object-Oriented Programming Fundamentals      ##
####################################################

####################################################
## 1. Inheritance
####################################################

print("\n1. Inherritence")
print("\nInheritance allows new child classes to be defined")
print("that inherit methods and variables from their parent class.")

# Using the Human class defined above as the base or parent class, we can
# define a child class, Superhero, which inherits variables like "species",
# "name", and "age", as well as methods, like "sing" and "grunt"
# from the Human class, but can also have its own unique properties.

# To take advantage of modularization by file you could place the classes above
# in their own files, say, human.py

# To import functions from other files use the following format
# from "filename-without-extension" import "function-or-class"

from learn_classes import Human

# Specify the parent class(es) as parameters to the class definition
class Superhero(Human):
    # 1.2.1 Overriding Class Attributes
    # Child classes can override their parent's attributes.
    # If the child class should inherit all of the parent's definitions without
    # any modifications, you can just use the "pass" keyword (and nothing else)
    # but in this case it is commented out to allow for a unique child class:
    # pass

    # Child classes can override their parents' attributes
    species = "Superhuman"

    # 1.2.2 Initializer Method
    # Child classes inherit the parent's constructor & can extend / override it.
    # This constructor inherits the "name" argument from the "Human" class and
    # adds the "superpower" and "movie" arguments:
    def __init__(self, name, movie=False,
                 superpowers=["super strength", "bulletproofing"]):

        # Add additional class attributes specific to the child class
        self.fictional = True
        self.movie = movie
        # be aware of mutable default values, since defaults are shared
        self.superpowers = superpowers

        # The "super" function lets you access the parent class's methods
        # that are overridden by the child, in this case, the __init__ method.
        # This calls the parent class constructor:
        super().__init__(name)

    # 1.2.3 Overriding Instance Methods (sing)
    def sing(self):
        return "Dun, dun, DUN!"

    # 1.2.4 Additional Instance Methods
    # Child classes can also define new methods unique to them.
    def boast(self):
        for power in self.superpowers:
            print(f"I wield the power of {power}!")


if __name__ == "__main__":
    # 1.3 Inheritance Demonstration
    print("\n1.3 Inheritance Demonstration")

    # Instantiate a Superhero object
    print('1.3.0 sup = Superhero(name="Tick")')
    sup = Superhero(name="Tick")

    # 1.3.1 Instance Type Checks
    print("\n1.3.1 Instance Type Checks:")
    print("Code: isinstance(sup, Human)")
    if isinstance(sup, Human):
        print("    Tick is an instance of Human")
    print("Code: type(sup) is Superhero")
    if type(sup) is Superhero:
        print("    Tick is specifically a Superhero")
    print("Code: type(sup) is Human")
    if type(sup) is Human:
        print("    Tick is specifically a Human")
    else:
        print("    Tick is specifically not a Human")

    # 1.3.2 Method Resolution Order (MRO)
    # Get the MRO used by both getattr() and super()
    # (the order in which classes are searched for an attribute or method)
    # This attribute is dynamic and can be updated
    # => (<class '__main__.Superhero'>,
    # => <class 'human.Human'>, <class 'object'>)
    print("\n1.3.2 Method Resolution Order (MRO):")
    print("Code: Superhero.__mro__")
    print("    MRO:", Superhero.__mro__)

    # 1.3.3 Calls Parent Method Using Child's Class Attribute
    print("\n1.3.3 Calls Parent Method Using Child's Class Attribute:")
    print("Code: sup.get_species()")
    print("    Species:", sup.get_species())

    # 1.3.4 Overridden Methods
    print("\n1.3.4 Overridden Methods:")
    print("Code: sup.sing()")
    print("    Singing:", sup.sing())

    # 1.3.5 Calls Parent Method
    print("\n1.3.5 Calls Parent Method:")
    print("Code: sup.say('Spoon')")
    sup.say("Spoon")

    # 1.3.6 Child Class-Specific Methods
    print("\n1.3.6 Child Class-Specific Methods:")
    print("Code: sup.boast()")
    # => I wield the power of super strength!
    # => I wield the power of bulletproofing!
    sup.boast()

    # 1.3.7 Inherited Property
    print("\n1.3.7 Inherited Property:")
    print("Code: sup.age = 31")
    sup.age = 31
    print("    Tick's age:", sup.age)

    # 1.3.8 Child Class-Specific Attribute
    # => False (see default value)
    print("\n1.3.8 Child Class-Specific Attribute:")
    print("Code: sup.movie")
    print("    Is Tick Oscar eligible?", sup.movie)

####################################################
## 2. Multiple Inheritance
####################################################

# Multiple inheritance allows a class to inherit attributes and methods
# from more than one parent class. This can be useful for combining 
# functionalities from different classes, but it also introduces complexity 
# because of method resolution order (MRO) and potential attribute conflicts.
# 
# This example demonstrates:
# 1. How multiple inheritance works in Python.
# 2. How to initialize attributes from multiple parent classes.
# 3. How MRO determines the order of method/attribute resolution.
# 4. Overriding methods and attributes in child classes.

# 2.1 Class Declarations

# A class representing a Bat
class Bat:
    species = "Baty"

    def __init__(self, can_fly=True):
        self.fly = can_fly

    # This class also has a "say" method
    def say(self, msg):
        msg = "... ... ..."
        return msg

    # And its own method
    def sonar(self):
        return "))) ... ((("

# A class representing Batman, inheriting from both Superhero and Bat
# order affects MRO
class Batman(Superhero, Bat):

    def __init__(self, *args, **kwargs):
        # Typically to inherit attributes you have to call super:
        # super(Batman, self).__init__(*args, **kwargs)
        # However we are dealing with multiple inheritance here, and super()
        # only works with the next base class in the MRO list.
        # So instead we explicitly call __init__ for all ancestors.
        # The use of *args and **kwargs allows for a clean way to pass
        # arguments, with each parent "peeling a layer of the onion".
        Superhero.__init__(self, "anonymous", movie=True,
                           superpowers=["Wealthy"], *args, **kwargs)
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        
        # Override the name attribute
        self.name = "Sad Affleck"

    def sing(self):
        return "nan nan nan nan nan batman!"

if __name__ == "__main__":
    # 2.2 Multiple Inheritance Demonstration
    print("\n2. Multiple Inheritance Demonstration")

    # 2.2.1 Instantiate Bat Class
    print("\n2.2.1 Instantiate Bat Class:")
    bat = Bat()
    print("Code: bat.say('hello')")
    print("    Bat says:", bat.say("hello"))
    print("Code: bat.fly")
    print("    Can Bat fly?", bat.fly)

    # 2.2.2 Instantiate Batman Class
    print("\n2.2.2 Instantiate Batman Class:")
    sup = Batman()

    # 2.2.3 Method Resolution Order (MRO)
    print("\n2.2.3 Method Resolution Order (MRO):")
    print("Code: Batman.__mro__")
    # => (<class '__main__.Batman'>,
    # => <class 'superhero.Superhero'>,
    # => <class 'human.Human'>,
    # => <class 'bat.Bat'>, <class 'object'>)
    print("    MRO:", Batman.__mro__)

    # 2.2.4 Calls Parent Method Using Child's Class Attribute
    print("\n2.2.4 Calls Parent Method Using Child's Class Attribute:")
    print("Code: sup.get_species()")
    print("    Species:", sup.get_species()) # => Superhuman

    # 2.2.5 Overridden Methods
    print("\n2.2.5 Overridden Methods:")
    print("Code: sup.sing()")
    print("    Singing:", sup.sing()) # => nan nan nan nan nan batman!

    # 2.2.6 Calls Method from First Parent Class
    print("\n2.2.6 Calls Method from First Parent Class:")
    print("Code: sup.say('I agree')")
    sup.say("I agree") # => Sad Affleck: I agree

    # 2.2.7 Calls Method from Second Parent Class
    print("\n2.2.7 Calls Method from Second Parent Class:")
    print("Code: sup.sonar()")
    print("    Sonar:", sup.sonar()) # => ))) ... (((

    # 2.2.8 Inherited Property
    print("\n2.2.8 Inherited Property:")
    print("Code: sup.age = 100")
    sup.age = 100
    print("    Batman's age:", sup.age)

    # 2.2.9 Inherited Attribute with Overridden Value
    # Inherited attribute from 2nd ancestor whose default value was overridden.
    print("\n2.2.9 Inherited Attribute with Overridden Value:")
    print("Code: sup.fly")
    print("    Can Batman fly?", sup.fly)