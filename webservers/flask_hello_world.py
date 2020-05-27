"""
Hello world HTTP app - using Flask.

    
This will pick 'name' from query parameters.
e.g. http://localhost:5000/?name=Visitor
"""
from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/')
def hello():
    """
    Handle GET request on the root path, using query parameters.
    """
    name = request.args.get("name", "World")
    
    return f"Hello, {escape(name)}!"
