
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Hjemside</h1>
    '''

@app.route('/meg')
def meg():
    return '''
    <h1>Om meg</h1>
    <p>Jeg er meg</p>
    '''

@app.route('/deg')
def deg():
    return '''
    <h1>Jeg vet hvor du bor</h1>
    <p>Jeg er under senga di i natt :)</p>
    '''

@app.route('/drikke')
def drikke():
    return '''
    <p> Vann </p>
    '''

app.run()