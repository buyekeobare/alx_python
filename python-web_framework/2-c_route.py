#! usr\bin\python3

'''
  Write a script that starts a Flask web application:
'''

from flask import Flask

'''
  Flask imported
'''

app = Flask(__name__)


@app.route("/")
def home():
  return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
  return "HBNB"


@app.route("/c/<text>")
def c(text):
  return("C {}".format(text.replace("_", " ")))


if __name__=="__main__":
  app.run(debug=True, port="5000")