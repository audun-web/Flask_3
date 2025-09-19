
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!doctype html>
    <html lang="no">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Hjem</title>
        <style>
            body {
                margin: 0;

                font-family: Arial, sans-serif;

                background: #f7f7f7;

                color: #222;
            }

            .container {
                max-width: 640px;

                margin: 40px auto;

                background: #ffffff;

                border: 1px solid #dddddd;

                border-radius: 8px;

                padding: 16px;
            }

            h1 {
                margin: 0 0 12px;
            }

            p {
                margin: 0;
            }
        </style>
    </head>
    <body>
        <main class="container">
            <h1>Hjemside</h1>
            <p>Velkommen!</p>
        </main>
    </body>
    </html>
    '''

@app.route('/meg')
def meg():
    return '''
    <!doctype html>
    <html lang="no">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Om meg</title>
        <style>
            body {
                margin: 0;

                font-family: Arial, sans-serif;

                background: #f7f7f7;

                color: #222;
            }

            .container {
                max-width: 640px;

                margin: 40px auto;

                background: #ffffff;

                border: 1px solid #dddddd;

                border-radius: 8px;

                padding: 16px;
            }

            h1 {
                margin: 0 0 12px;
            }

            p {
                margin: 0;
            }
        </style>
    </head>
    <body>
        <main class="container">
            <h1>Om meg</h1>
            <p>Jeg er meg</p>
        </main>
    </body>
    </html>
    '''

@app.route('/deg')
def deg():
    return '''
    <!doctype html>
    <html lang="no">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Til deg</title>
        <style>
            body {
                margin: 0;

                font-family: Arial, sans-serif;

                background: #f7f7f7;

                color: #222;
            }

            .container {
                max-width: 640px;

                margin: 40px auto;

                background: #ffffff;

                border: 1px solid #dddddd;

                border-radius: 8px;

                padding: 16px;
            }

            h1 {
                margin: 0 0 12px;
            }

            p {
                margin: 0;
            }
        </style>
    </head>
    <body>
        <main class="container">
            <h1>Jeg vet hvor du bor</h1>
            <p>Jeg er under senga di i natt :)</p>
        </main>
    </body>
    </html>
    '''

@app.route('/drikke')
def drikke():
    return '''
    <!doctype html>
    <html lang="no">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Drikke</title>
        <style>
            body {
                margin: 0;

                font-family: Arial, sans-serif;

                background: #f7f7f7;

                color: #222;
            }

            .container {
                max-width: 640px;

                margin: 40px auto;

                background: #ffffff;

                border: 1px solid #dddddd;

                border-radius: 8px;

                padding: 16px;
            }

            h1 {
                margin: 0 0 12px;
            }

            ul {
                margin: 0;

                padding-left: 18px;
            }
        </style>
    </head>
    <body>
        <main class="container">
            <h1>Drikke</h1>
            <ul>
                <li>Vann</li>
                <li>Juice</li>
                <li>Brus</li>
            </ul>
        </main>
    </body>
    </html>
    '''

app.run()