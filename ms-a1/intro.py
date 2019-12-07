# Load Flask
from flask import Flask

# Create the app

app = Flask(__name__)

# Add a route


@app.route('/')
# Define what happens
def index():
    # Return some content to the user
    return "<h1>Hello, World</h1>"
