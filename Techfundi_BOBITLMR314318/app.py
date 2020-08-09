from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/medical-status.html')
def medicalStatus():
    return render_template('/medical-status.html')


@app.route('/background-status.html')
def backgroundStatus():
    return render_template('background-status.html')


@app.route('/placeVisited-status.html')
def placeVisited():
    return render_template('placeVisited-status.html')
