Why Python programming is awesome
What is OOP
“first-class everything”
What is a class
What is an object and an instance
What is the difference between a class and an object or instance
What is an attribute
What are and how to use public, protected and private attributes
What is self
What is a method
What is the special **init** method and how to use it
What is Data Abstraction, Data Encapsulation, and Information Hiding
What is a property
What is the difference between an attribute and a property in Python
What is the Pythonic way to write getters and setters in Python
How to dynamically create arbitrary new attributes for existing instances of a class
How to bind attributes to object and classes
What is the **dict** of a class and/or instance of a class and what does it contain
How does Python find the attributes of an object or class
How to use the getattr function

# Tasks

0. Square with size

Write a class Square that defines a square by:

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
Why?

Why size is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

1. Size validation

Write a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with optional size: def **init**(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
You are not allowed to import any module

2. Area of a square

Write a class Square that defines a square by: (based on 1-square.py)

Private instance attribute: size
Instantiation with optional size: def **init**(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Public instance method: def area(self): that returns the current square area
You are not allowed to import any module

3. Access and update private attribute

Write a class Square that defines a square by: (based on 2-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Instantiation with optional size: def **init**(self, size=0):
Public instance method: def area(self): that returns the current square area
You are not allowed to import any module
Why?

Why a getter and setter?

Reminder: size is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

4. Printing a square

Write a class Square that defines a square by: (based on 3-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Instantiation with optional size: def **init**(self, size=0):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
You are not allowed to import any module

# Evaluation Quiz

0. In this following code, what is \_\_password?

class User:
id = 89
name = "no name"
\_\_password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

A private class attribute

1. What do these lines print?

> > > class User:
> > > id = 89
> > > name = "no name"
> > > \_\_password = None
> > >
> > >     def __init__(self, new_name=None):
> > >         self.is_new = True
> > >         if new_name is not None:
> > >             self.name = new_name
> > >
> > > u = User()
> > > u.id

89

2. In this following code, what is User?

class User:
id = 89
name = "no name"
\_\_password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

A class

3. What do these lines print?

> > > class User:
> > > id = 89
> > > name = "no name"
> > > \_\_password = None
> > >
> > >     def __init__(self, new_name=None):
> > >         self.is_new = True
> > >         if new_name is not None:
> > >             self.name = new_name
> > >
> > > u = User()
> > > u.name

no name

4. What do these lines print?

> > > class User:
> > > id = 89
> > > name = "no name"
> > > \_\_password = None
> > >
> > >     def __init__(self, new_name=None):
> > >         self.is_new = True
> > >         if new_name is not None:
> > >             self.name = new_name
> > >
> > > u = User("John")
> > > u.name

John

5. In this following code, what is is_new?

class User:
id = 89
name = "no name"
\_\_password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

A public instance attribute

6. In this following code, what is id?

class User:
id = 89
name = "no name"
\_\_password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

A public class attribute

7. What do these lines print?

> > > class User:
> > > id = 89
> > > name = "no name"
> > > \_\_password = None
> > >
> > >     def __init__(self, new_name=None):
> > >         self.is_new = True
> > >         if new_name is not None:
> > >             self.name = new_name
> > >
> > > u = User()
> > > u.is_new

True
