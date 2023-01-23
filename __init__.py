from .qopy import Client
from .cli import main
import os
from flask import Flask

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = Flask(__name__)


    @app.route('/')
    def hello():
        return 'Hello, World!'