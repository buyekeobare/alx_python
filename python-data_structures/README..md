# Python - Data Structures: Lists, Tuples

Why Python programming is awesome
What are lists and how to use them
What are the differences and similarities between strings and lists
What are the most common methods of lists and how to use them
How to use lists as stacks and queues
What are list comprehensions and how to use them
What are tuples and how to use them
When to use tuples versus lists
What is a sequence
What is tuple packing
What is sequence unpacking
What is the del statement and how to use it

# Tasks

0. Can you C me now?

Write a function that removes all characters c and C from a string.

Prototype: def no_c(my_string):
The function should return the new string
You are not allowed to import any module
You are not allowed to use str.replace()

1. Lists of lists = Matrix

Write a function that prints a matrix of integers.

Prototype: def print_matrix_integer(matrix=[[]]):
Format: see example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers

2. More returns!

Write a function that returns a tuple with the length of a string and its first character.

Prototype: def multiple_returns(sentence):
If the sentence is empty, the first character should be equal to None
You are not allowed to import any module

# Evaluation Quiz

0. What do these lines print?

> > > a = [1, 2, 3, 4]
> > > b = a
> > > a[2] = 10
> > > b

[1, 2, 10, 4]

1. What do these lines print?

> > > a = [1, 2, 3, 4]
> > > a[-3]

2

2. What do these lines print?

> > > a = [1, 2, 3, 4]
> > > a[1:3]

[2, 3]

3. What do these lines print?

> > > a = [1, 2, 3, 4]
> > > a[0]

1

4. What do these lines print?

> > > a = [1, 2, 3, 4]
> > > b = a
> > > b

[1, 2, 3, 4]

5. What do these lines print?

> > > a = [1, 2, 3, 4]
> > > a[2] = 10
> > > a

[1, 2, 10, 4]

6. What do these lines print?

> > > a = [1, 2, 3, 4]
> > > len(a)

4

7. What do these lines print?

> > > a = [1, 2, 3, 4]
> > > b = a
> > > a[2] = 10
> > > a

[1, 2, 10, 4]

8. What do these lines print?

> > > a = [1, 2, 3, 4]
> > > a[-1]

4

9. What do these lines print?

> > > a = [1, 2, 3, 4]
> > > a.append(5)
> > > len(a)

5
