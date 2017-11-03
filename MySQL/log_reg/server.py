from flask import Flask, request, redirect, session, render_template, flash, get_flashed_messages
import re
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = 'keykey'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'log_reg')
email_reg = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    messages = get_flashed_messages()
    return render_template('index.html', messages = messages)

@app.route('/register', methods = ['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_pass = request.form['confirm_pass']

    errors = []

    if len(first_name) == 0 or len(first_name) < 2 or not first_name.isalpha():
        errors.append('First Name cannot be blank, must be letters only and at least 2 characters long!')

    if len(last_name) == 0 or len(last_name) < 2 or not last_name.isalpha():
        errors.append('Last Name cannot be blank, must be letters only and at least 2 characters long!')

    if len(email) == 0 or not email_reg.match(email):
        errors.append('Email format is not valid!')

    if len(password) < 8 or len(password) == 0:
        errors.append('Password must be at least 8 characters long!')

    if password != confirm_pass:
        errors.append('Passwords must match!')

    if errors:
        for error in errors:
            flash(error)
        return redirect('/')

    else:
        pw_hash = bcrypt.generate_password_hash(password)
        query = "INSERT INTO users (first_name, last_name, email, pw_hash) VALUES (:first_name, :last_name, :email, :pw_hash)"
        data = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'pw_hash': pw_hash
                }
        mysql.query_db(query, data)
        return render_template('success.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = {'email': email}
    user = mysql.query_db(query,data)

    if len(email) == 0 or len(password) == 0:
        flash('Both Email and Password are required to login!')
        return redirect('/')

    if bcrypt.check_password_hash(user[0]['pw_hash'], password):
        return render_template('success.html')

    else:
        flash('Incorrect Email or Password!')
        return redirect('/')

app.run(debug=True)
