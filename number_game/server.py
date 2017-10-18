from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "very_secret_123"
@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 101)
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def guess():
    if session['number'] == int(request.form['guess']):
        session['result'] = 'correct'
    elif session['number'] < int(request.form['guess']):
        session['result'] = 'high'
    else:
        session['result'] = 'low'

    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('number')
    session.pop('result')
    return redirect('/')

app.run(debug=True)
