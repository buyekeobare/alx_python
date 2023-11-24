# Learning Objectives

- At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General

- What is an API?
- What is a REST API?
- What are microservices?
- What is the CSV format?
- What is the JSON format?
- Pythonic Package and module name style?
- Pythonic Class name style?
- Pythonic Variable name style?
- Pythonic Function name style?
- Pythonic Constant name style?
- Significance of CapWords or CamelCase in Python?

## Tasks

### 0. Gather data from an API

- Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

NB: The endpoint for access specific TODO items for an employee with ID = 1 will be https://jsonplaceholder.typicode.com/users/1/todos and the endpoint to get specific employee details will be https://jsonplaceholder.typicode.com/users/1

#### Requirements:

- You must use urllib or requests module
- The script must accept an integer as a parameter, which is the employee ID
- The script must display on the standard output the employee TODO list progress in this exact format:
- First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
  where:
- EMPLOYEE_NAME: name of the employee
- NUMBER_OF_DONE_TASKS: number of completed tasks
- TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
- Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

### 1. Export to CSV

- Using what you did in the task #0, extend your Python script to export data in the CSV format.

#### Requirements:

- Records all tasks that are owned by this employee
- Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv

### 2. Export to JSON

- Using what you did in the task #0, extend your Python script to export data in the JSON format.

#### Requirements:

- Records all tasks that are owned by this employee
- Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": - - TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
- File name must be: USER_ID.json

### 3. Dictionary of list of dictionaries

- Using what you did in the task #0, extend your Python script to export data in the JSON format.

#### Requirements:

- Records all tasks from all employees
- Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
- File name must be: todo_all_employees.json

###

# Evalution Quiz

## Responses

0. What is the purpose of URL encoding?

To convert special characters in a URL to a valid format

1. What is the purpose of versioning in APIs?

To allow multiple API versions to coexist and support backward compatibility

2. What is the purpose of an API key?

It is used to authenticate and authorize access to an API

3. What are microservices?

Small, independent, and loosely coupled services that work together

4. What is a REST API?

An API that follows the principles of Representational State Transfer

5. How can you handle paginated API responses in Python?

By making multiple API requests and merging the responses together

6. How can you handle errors and exceptions when making API requests in Python?

By using try-except blocks to catch and handle exceptions

7. How can you authenticate API requests using an API key?

By including the API key in the request headers

8. What is the purpose of rate limiting in API usage?

To limit the number of requests an API consumer can make within a specified time period

9. What is the significance of CapWords or CamelCase in Python?

It is a naming convention for class names in Python

10. What does API stand for?

Application Programming Interface

11. What is the difference between PUT and POST HTTP methods?

PUT is used for updating resources, while POST is used for creating resources

12. What is the Pythonic variable name style?

snake_case

13. What is the Pythonic class name style?

PascalCase

14. What is the JSON format?

JavaScript Object Notation format used for storing hierarchical data

15. What is the Pythonic function name style?

snake_case

16. What is the Pythonic package and module name style?

snake_case

17. What is the CSV format?

Comma-Separated Values format used for storing tabular data

18. What is the difference between synchronous and asynchronous API requests?

Synchronous requests block the code execution until a response is received, while asynchronous requests allow the code execution to continue while waiting for a response.

19. What is the Pythonic constant name style?

snake_case
