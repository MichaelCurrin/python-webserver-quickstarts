from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/')
def hello():
    """
    This will pick 'name' from query parameters.
    e.g. http://localhost:5000/?name=Visitor
    """
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
