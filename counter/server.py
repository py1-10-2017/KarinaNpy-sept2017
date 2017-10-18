from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Secure123'
@app.route('/')
def index():
    try:
        session['index']+=1
    except:
        session['index']=1
    return render_template('index.html')
app.run(debug=True)
