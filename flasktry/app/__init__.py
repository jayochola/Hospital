
from flask import Flask
import os

def main():
    app= Flask(__name__)
    SECRET_KEY = os.urandom(14)
    app.config[SECRET_KEY]=SECRET_KEY
    return app