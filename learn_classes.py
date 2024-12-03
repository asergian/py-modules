####################################################
##  Classes                                       ##
##  Object-Oriented Programming Fundamentals      ##
####################################################

####################################################
## 1. Classes
####################################################

# When a Python interpreter reads a source file it executes all its code.
# This __name__ check makes sure this code block is only executed when this
# module is the main program.

if __name__ == "__main__":
    print("\n1. Classes")
    print("\nThey are the foundation of Object-Oriented Programming in Python.")
    print("They allow you to create custom data types,"),
    print("encapsulate data and behavior,")
    print("and implement inheritance and polymorphism.")

# 1.1 Basic Class Definition
class Human:
    # 1.1.1 Class Attribute
    species = "H. sapiens"

    # 1.1.2 Initializer Method
    # This is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by Python but that live in user-controlled
    # namespaces. Methods(or objects or attributes) like: __init__, __str__,
    # __repr__ etc. are called special methods (or sometimes called dunder
    # methods). You should not invent such names on your own.
    def __init__(self, name):
        self.name = name # Assign the argument to the instance's name attribute
        
        # the leading underscore indicates the "age" property is
        # intended to be used internally
        # do not rely on this to be enforced: it's a hint to other devs
        self._age = 0 # Initialize property

    # 1.1.3 Instance Methods. All methods take "self" as the first argument
    def say(self, msg):
        print(f"{self.name}: {msg}")

    def sing(self):
        return "yo... yo... microphone check... one two... one two..."

    # 1.1.4 Class Method. These are shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # 1.1.5 Static Method, called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    # 1.1.6 Property Decorators
    # A property is just like a getter.
    # It turns the method age() into a read-only attribute of the same name.
    # There's no need to write trivial getters and setters in Python, though.
    @property
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age

if __name__ == "__main__":
    # 1.2 Class Demonstration
    print("\n1.2 Class Demonstration")

    # Instantiate classes
    # ian and joel are instances of type Human; i.e., they are Human objects.
    print('1.2.0 ian = Human(name="Ian") \\ joel = Human("Joel")')
    ian = Human(name="Ian")
    joel = Human("Joel")

    # 1.2.1 Instance Methods
    print("\n1.2.1 Instance Methods:")
    print("Code: ian.say('hi')")
    ian.say("hi")                     
    print("Code: joel.say('hello')")
    joel.say("hello")                 

    # 1.2.2 Class Method
    print("\n1.2.2 Class Method:")
    print("Code: ian.get_species()")
    print("    Initial species:", ian.get_species())

    # 1.2.3 Modifying Class Attribute
    print("\n1.2.3 Modifying Class Attribute:")
    print("Code: Human.species = 'H. neanderthalensis'")
    Human.species = "H. neanderthalensis"
    print("    Ian's species:", ian.get_species())
    print("    Joel's species:", joel.get_species())

    # 1.2.4 Static Method
    print("\n1.2.4 Static Methods:")
    print("Code: Human.grunt()")
    print("    Human.grunt() =", Human.grunt())

    # Static methods can be called by instances too
    print("Code: ian.grunt()")
    print("    ian.grunt() =", ian.grunt())

    # 1.2.5 Property Demonstration
    print("\n1.2.5 Property Demonstration:")
    print("Code: ian.age = 42")
    ian.age = 42
    print("    Ian's age:", ian.age)
    print("    Joel's age:", joel.age)

    # 1.2.6 Property Deletion
    print("\n1.2.6 Property Deletion:")
    print("Code: del ian.age")
    del ian.age
    print("    Ian's age after deletion: (raises AttributeError if accessed)")
    try:
        ian.age
    except AttributeError as E:
        print("1.2.7 AttributeError accessing ian.age")
    else:
        print("1.2.7 No issues accessing ian.age")