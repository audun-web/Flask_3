import re
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Hjemside</h1>
    '''

@app.rouge('/meg')
def meg():
    return '''
    <h1>Om meg</h1>
    <p>Jeg er meg</p>
    '''