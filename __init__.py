from flask import Flask

def create_app():
    app = Flask(__name__)

    from . import routes  # Import routes

    return app
