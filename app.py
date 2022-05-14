# 9.4.3 Set Up Flask and Create a Route
# 1.) Install Flask.
# 2.) Create a new Python file.
# 3.) Import the Flask dependency.
# 4.) Create a new Flask app instance.
# 5.) Create Flask routes.
# 6.) Run a Flask app


# Create a New Python File and Import the Flask Dependency
from flask import Flask

# Create a New Flask App Instance
app = Flask(__name__)

# Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'

# Run a Flask App
# set FLASK_APP=app.py
# 
# flask run