Why Python programming is awesome
What is a superclass, baseclass or parentclass
What is a subclass
How to list all attributes and methods of a class or instance
When can an instance have new attributes
How to inherit class from another
How to define a class with multiple base classes
What is the default class every class inherit from
How to override a method or attribute inherited from the base class
Which attributes or methods are available by heritage to subclasses
What is the purpose of inheritance
What are, when and how to use isinstance, issubclass, type and super built-in functions

# Tasks

0. Exact same object

Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

Prototype: def is_same_class(obj, a_class):
You are not allowed to import any module

1. Same class or inherit from

Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

Prototype: def is_kind_of_class(obj, a_class):
You are not allowed to import any module

2. Only sub class of

Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

Prototype: def inherits_from(obj, a_class):
You are not allowed to import any module

3. Geometry module

Write an empty class BaseGeometry.

You are not allowed to import any module

4. Improve Geometry

Write a class BaseGeometry (based on 3-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
You are not allowed to import any module

5. Integer validator

Write a class BaseGeometry (based on 4-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
Public instance method: def integer_validator(self, name, value): that validates value:
you can assume name is always a string
if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
You are not allowed to import any module

6. Rectangle

Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).

Instantiation with width and height: def **init**(self, width, height):
width and height must be private. No getter or setter
width and height must be positive integers, validated by integer_validator

7. Full rectangle

Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py). (task based on 6-rectangle.py)

Instantiation with width and height: def **init**(self, width, height)::
width and height must be private. No getter or setter
width and height must be positive integers validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>

8. Square #1

Write a class Square that inherits from Rectangle (7-rectangle.py):

Instantiation with size: def **init**(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented

# Evalaution Quiz

0. What does "first-class everything" mean in Python?

Python allows functions to be assigned to variables and passed as arguments

1. What is the method called when a child class overrides a method of the parent class?

Overriding method

2. What is the output of the following code?
   my_list = [1, 2, 3, 4, 5]
   result = [x * 2 for x in my_list if x % 2 == 0]
   print(result)

[2, 4]

3. Which built-in function is used to check if an object is an instance of a particular class or its subclasses?

isinstance()

4. Which of the following statements about inheritance is true?

Inheritance allows a class to inherit both attributes and methods from a parent class.

5. What is OOP?

Object-Oriented Programming

6. What is the correct way to remove an element from a list named my_list using its value?

my_list.remove(value)

7. What is the purpose of the self parameter in Python methods?

It refers to the current object instance

8. What is an attribute in Python?

A special type of variable that belongs to an object

9. What is a method in Python?

A function defined inside a class

10. What is the output of the following code?
    my_string = "Hello, World!"
    print(my_string[::-1])

"dlroW ,olleH"

11. What is the correct way to open a file named "data.txt" in Python for writing?

file = open("data.txt", "w")

12. What does the len() function in Python return?

The length of a string
The number of elements in a list, tuple, or set
The number of key-value pairs in a dictionary

13. What is the difference between a class and an object or instance?

An object is an instance of a class

14. Why is Python programming awesome?

It is easy to learn and read
It has a large and active community
It has extensive libraries and frameworks

15. What are public, protected, and private attributes in Python?

Access modifiers that control the visibility and accessibility of attributes

16. What is the term used to describe a class that inherits properties and methods from another class?

Derived class

17. What is a class in Python?

A blueprint for creating objects

18. What is the special **init** method and how is it used?

It initializes the class object and is called when a new instance is created

20. What do these lines print?

class Base():
""" My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
""" My User class """

    def __init__(self):
        super().__init__()
        self.id += 99

u = User()
print(u.id)

100

1. What do these lines print?

class Base():
""" My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
""" My User class """
pass

u = User()
print(u.id)

1

2. What do these lines print?

class Base():
""" My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
""" My User class """

    def __init__(self):
        self.id = 89

u = User()
print(u.id)

89

3. What do these lines print?

class Base():
""" My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

b = Base()
print(b.id)

1

4. What do these lines print?

class Base():
""" My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
""" My User class """

    def __init__(self):
        self.id = 89
        super().__init__()

u = User()
print(u.id)

1

5. What do these lines print?

class Base():
""" My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
""" My User class """

    def __init__(self):
        super().__init__()

u = User()
print(u.id)

1

6. What do these lines print?

class Base():
""" My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
""" My User class """
pass

for i in range(4):
u = User()
print(u.id)

4

7. What do these lines print?

class Base():
""" My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
""" My User class """

    def __init__(self):
        super().__init__()
        self.id = 89

u = User()
print(u.id)

89

8. What do these lines print?

class Base():
""" My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

for i in range(3):
b = Base()
print(b.id)

3

9. What do these lines print?

class Base():
""" My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
""" My User class """
pass

b = Base()
u = User()
print(u.id)

2
