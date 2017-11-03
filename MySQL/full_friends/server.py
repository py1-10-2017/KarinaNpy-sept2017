from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends = friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (`first_name`, `last_name`, `email`, `created_at`, `updated_at`) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email']
            }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<friend_id>/edit')
def edit(friend_id):
    return render_template('edit.html')


@app.route('/friends/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE id = :id"
    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'id': friend_id
            }
    mysql.query_db(query,data)
    return redirect('/')


app.run(debug=True)
