Requirements
General
Recommended editors: Visual studio code
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
Your files will be executed with MySQLdb version 1.3.x
Your files will be executed with SQLAlchemy version 1.2.x
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7.\*)
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(**import**("my_module").**doc**)')
All your classes should have a documentation (python3 -c 'print(**import**("my_module").MyClass.**doc**)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(**import**("my_module").my_function.**doc**)' and python3 -c 'print(**import**("my_module").MyClass.my_function.**doc**)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
You are not allowed to use execute with sqlalchemy

# Tasks

0. Get all states

Write a script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported

1. Filter states

Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported

2. Filter states by user input

Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You must use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported

3. SQL Injection...

Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT \* FROM states WHERE name = '" as an input?

What? Empty?

Yes, it’s an SQL injection to delete all records of a table…

Once again, write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!

Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported

4. Cities by states

Write a script that lists all cities from the database hbtn_0e_4_usa

Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
Results must be displayed as they are in the example below
Your code should not be executed when imported

5. All cities by state

Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
The results must be displayed as they are in the example below
Your code should not be executed when imported

6. First state model

Write a python file that contains the class definition of a State and an instance Base = declarative_base():

State class:
inherits from Base Tips
links to the MySQL table states
class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
class attribute name that represents a column of a string with maximum 128 characters and can’t be null
You must use the module SQLAlchemy
Your script should connect to a MySQL server running on localhost at port 3306
WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)

7. All states via SQLAlchemy

Write a script that lists all State objects from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
The results must be displayed as they are in the example below
Your code should not be executed when imported

8. First state

Write a script that prints the first State object from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
The state you display must be the first in states.id
You are not allowed to fetch all states from the database before displaying the result
The results must be displayed as they are in the example below
If the table states is empty, print Nothing followed by a new line
Your code should not be executed when imported

9. Contains `a`

Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
The results must be displayed as they are in the example below
Your code should not be executed when imported

# Evaluation Quiz

0. How do you connect to a MySQL database from a Python script?

Using the connect() function from the pymysql module

1. How do you delete rows from a MySQL table using an ORM class?

By using the DELETE statement in the query with the appropriate conditions

2. How do you SELECT rows in a MySQL table from a Python script?

Using the fetchall() method from the MySQL cursor object

3. How do you define a primary key for a MySQL table in an ORM class?

By using the @id decorator above the attribute definition

4. How do you update rows in a MySQL table using an ORM class?

By calling the update() method of the class with the desired values

5. How do you map a Python Class to a MySQL table using an ORM?

By defining a class that represents the table and inherits from the Base class of the ORM

6. How do you handle transactions in MySQL using an ORM class?

By using the START TRANSACTION statement in the query

7. What does the commit() method do in MySQL when using an ORM class?

Saves the changes made to the database permanently

8. How do you query rows from a MySQL table using an ORM class?

By calling the select() method of the class

9. How do you close the database connection when using an ORM class in MySQL?

By calling the disconnect() method of the class

10. How do you INSERT rows in a MySQL table from a Python script?

Using the execute() method from the MySQL cursor object

11. How do you retrieve all columns from a table using an ORM class?

By using the SELECT \* statement in the query

12. How do you define a column with a unique constraint in an ORM class?

By using the @column decorator with the unique=True parameter

13. How do you handle database errors when using an ORM class in MySQL?

By using the try...except block to catch and handle exceptions

14. How do you perform an INNER JOIN between two tables using an ORM?

By specifying the relationship between the tables in the class definitions

15. Why is Python programming considered awesome?

It has a simple and readable syntax
It is a high-performance language
It supports both procedural and object-oriented programming

16. What does ORM stand for?

Object-Relational Mapping

17. How do you roll back a transaction in MySQL using an ORM class?

By using the ROLLBACK statement in the query

18. How do you specify the table name for an ORM class?

By setting the **tablename** attribute in the class definition

19. How do you execute raw SQL queries in MySQL using an ORM class?

By calling the query() method of the class with the raw SQL query
