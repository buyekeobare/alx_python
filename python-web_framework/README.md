Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What is a Web Framework
How to build a web framework with Flask
How to define routes in Flask
What is a route
How to handle variables in a route
What is a template
How to create a HTML response in Flask by using a template
How to create a dynamic template (loops, conditions…)
How to display in HTML data from a MySQL database

## Tasks

0. Hello Flask!

Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition

1. HBNB

Copy the previous task to a new script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
You must use the option strict_slashes=False in your route definition

2. C is fun!

Copy the previous task to a new script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable (replace underscore \_ symbols with a space )
You must use the option strict_slashes=False in your route definition

3. Python is cool!

Copy the previous task to a new script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
You must use the option strict_slashes=False in your route definition

4. Is it a number?

Copy the previous task to a new script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
You must use the option strict_slashes=False in your route definition

5. Number template

Copy the previous task to a new script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
You must use the option strict_slashes=False in your route definition

6. Odd or even?

Copy the previous task to a new script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
/number_odd_or_even/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n is even|odd” inside the tag BODY
You must use the option strict_slashes=False in your route definition

# Evaluation Quiz

0. How can you handle file uploads in Flask?

By using the request object in Flask to access the uploaded file

1. How do you install Flask?

By using the command pip install flask

2. How can you create an HTML response in Flask using a template?

By using the render_template() function in Flask
now

3. What is a web framework?

A collection of libraries and tools that simplify web development

4. How can you display data from a MySQL database in HTML using Flask?

By passing the data from the Flask route function to the template

5. How can you deploy a Flask application to a production server?
   Score: 0.0

By using a cloud platform such as Heroku or AWS

6. What is a route in Flask?
   Score: 0.0

A URL pattern that maps to a specific function in Flask

7. How can you pass data from a Flask route function to a template?

By using the render_template() function and passing the data as arguments

8. What is a template in Flask?

A dynamic HTML page that can be rendered with data in Flask

9. What is the purpose of Flask's @app.route() decorator?
   Score: 1.0

To define the URL route for a Flask application

10. What is Flask-WTF used for in Flask?

To handle form validations and CSRF protection

11. How can you create a dynamic template in Flask?

By using template tags and expressions in the HTML template

12. How can you handle user authentication in Flask?

By using third-party libraries such as Flask-Login or Flask-Auth

13. How can you build a web framework with Flask?

By installing Flask using pip
By creating a new virtual environment
By defining routes and handling requests in Flask
By configuring database settings in Flask

14. What is the purpose of Flask's render_template() function?

To render dynamic HTML pages using data in Flask

15. What is Flask-Migrate used for in Flask?

To handle database migrations and schema changes

16. How can you handle form submissions in Flask?

By using the request object in Flask to access form data

17. What is the purpose of using the url_for() function in Flask?

To redirect the user to a different page in Flask

18. How do you handle variables in a route in Flask?

By passing the variable as a parameter to the route function in Flask

19. What is the role of a Flask route function?

To handle incoming HTTP requests and return an HTTP response
