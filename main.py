import json
import requests
from recognizer import *
from flask import Flask, render_template, flash, request
app = Flask(__name__)

@app.route('/' , methods = ['GET', 'POST'])
def index():
    data = []
    data = x()
    return render_template('index.html' , data = data)

if __name__ == "__main__":
    app.run(debug=True)
