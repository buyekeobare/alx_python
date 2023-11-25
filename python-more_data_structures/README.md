# Python - More Data Structures: Set, Dictionary

Why Python programming is awesome
What are set and how to use them
What are the most common methods of set and how to use them
When to use sets versus lists
How to iterate into a set
What are dictionary and how to use them
When to use dictionaries versus lists or sets
What is a key in a dictionary
How to iterate into a dictionary
What is a lambda function
What is map, reduce and filter functions

# Tasks

0. Squared simple

Write a function that computes the square value of all integers of a matrix.

Prototype: def square_matrix_simple(matrix=[]):
matrix is a 2 dimensional array
Returns a new matrix:
Same size as matrix
Each value should be the square of the value of the input
Initial matrix should not be modified
You are not allowed to import any module
You are allowed to use regular loops, map, etc.

1. Present in both

Write a function that returns a set of common elements in two sets.

Prototype: def common_elements(set_1, set_2):
You are not allowed to import any module

2. Update dictionary

Write a function that replaces or adds key/value in a dictionary.

Prototype: def update_dictionary(a_dictionary, key, value):
key argument will be always a string
value argument will be any type
If a key exists in the dictionary, the value will be replaced
If a key doesn’t exist in the dictionary, it will be created
You are not allowed to import any module

3. Best score

Write a function that returns a key with the biggest integer value.

Prototype: def best_score(a_dictionary):
You can assume that all values are only integers
If no score found, return None
You can assume all students have a different score
You are not allowed to import any module

4. Multiply by using map

Write a function that returns a list with all values multiplied by a number without using any loops.

Prototype: def multiply_list_map(my_list=[], number=0):
Returns a new list:
Same length as my_list
Each value should be multiplied by number
Initial list should not be modified
You are not allowed to import any module
You have to use map
Your file should be max 3 lines

# Evaluation Quiz

0. Which of the following is an immutable data structure in Python?

Tuple

1. What is the purpose of the lambda keyword in Python?

It is used to create anonymous functions.

2. What is the correct way to create an empty dictionary in Python?

Both first and second option are correct.

3. What does the following code snippet print?
   numbers = [1, 2, 3, 4, 5]
   for num in numbers:
   if num == 3:
   break
   print(num)
   else:
   print("Finished")

1 2

4. What is the output of the following code snippet?
   numbers = [1, 2, 3, 4, 5]
   result = map(lambda x: x \* 2, numbers)
   print(list(result))

[2, 4, 6, 8, 10]

5. Which data structure in Python is unordered and does not allow duplicate values?

Set

6. How do you add an element to a list in Python?

Using the append() method.
Using the insert() method.
Using the extend() method.

7. Which of the following is used to filter elements from a sequence based on a condition in Python?

filter

8. How can you handle errors and exceptions in Python?

Using the try and except statements to catch and handle exceptions.

9. What is the purpose of the try and finally blocks in exception handling?

The try block is used to catch and handle exceptions, while the finally block is used to specify code that should always be executed.

10. What is the purpose of the reduce function in Python?

It is used to reduce a sequence of elements to a single value.

11. What is the purpose of the pass statement in Python?

It is used to specify an empty code block.

12. How do you check if a key exists in a dictionary in Python?

Using the in keyword.

13. What is the purpose of the import statement in Python?

It allows you to include external libraries or modules in your code.

14. How do you access the value associated with a specific key in a dictionary?

By using square brackets and specifying the key.

15. What do these lines print?

> > > for i in [1, 2, 3, 4]:
> > > print(i, end=" ")

1 2 3 4

16. What do these lines print?

> > > a = { 'id': 89, 'name': "John" }
> > > a.get('age')

Nothing

17. What do these lines print?

> > > a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
> > > a.get('projects')[3]

4

18.What do these lines print?

> > > a = { 'id': 89, 'name': "John" }
> > > a['id']

89

19. What do these lines print?

> > > for i in range(0, 3):
> > > print(i, end=" ")

0 1 2

20. What do these lines print?

> > > a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }
> > > a.get('friends')[-1].get("name")

Amy

21. What do these lines print?

> > > for i in [1, 3, 4, 2]:
> > > print(i, end=" ")

1 3 4 2

22. What do these lines print?

> > > a = { 'id': 89, 'name': "John" }
> > > a.get('age', 0)

0

23. What do these lines print?

> > > for i in range(1, 4):
> > > print(i, end=" ")

1 2 3

24. What do these lines print?

> > > a = { 'id': 89, 'name': "John" }
> > > a.get('id')

89

25. What do these lines print?

> > > a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
> > > a.get('projects')

[1, 2, 3, 4]

26. What do these lines print?

> > > for i in ["Hello", "Holberton", "School", 98]:
> > > print(i, end=" ")

Hello Holberton School 98
