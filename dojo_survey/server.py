from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'secrecy1234'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    valid = True
    if len(request.form['name']) == 0:
        flash('Name cannot be empty!')
        valid = False
    if len(request.form['comment']) == 0:
        flash('Comment cannot be empty!')
        valid = False
    if len(request.form['comment']) > 120:
        flash('Comment cannot be longer than 120 characters')
        valid = False

    if valid:
        return redirect('/result')
    if not valid:
        return redirect('/')

@app.route('/result')
def result():
    return render_template('result.html', a=request.form['name'], b=request.form['location'], c=request.form['language'], d=request.form['comment'])
app.run(debug=True)
