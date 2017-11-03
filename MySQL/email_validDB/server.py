import mysqlconnection
import re
from flask import Flask, render_template, redirect, session, flash, request, get_flashed_messages
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "mykey"

email_reg = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
connection = mysqlconnection.MySQLConnector(app, 'db')

@app.route('/')
def index():
    messages = get_flashed_messages()
    return render_template('index.html', messages = messages)

@app.route('/add_user', methods=["POST"])
def add():
    if len(request.form['email']) == 0 or not re.match(email_reg, request.form['email']):
        flash('Email is not valid!')
        return redirect('/')

    else:
        connection.query_db("""
        INSERT INTO users (`email`, `created_at`, `updated_at`) VALUES('{}', NOW(), NOW())
        """.format(request.form['email']))
        return redirect('/users')

@app.route('/users')
def users():
    all_users = connection.query_db("SELECT * FROM users")
    return render_template('users.html', users = all_users)

app.run(debug=True)
