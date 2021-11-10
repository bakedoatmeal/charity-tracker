from flask import Flask, render_template
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for

client = MongoClient()
db = client.Donations
users = db.users

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage"""
    msg = "hello!"
    return render_template('users_index.html', users=users.find())

@app.route('/users')
def users_index():
    return render_template('users_index.html', users = users.find())

@app.route('/users/new')
def users_new():
    return render_template('users_new.html')

@app.route('/users', methods=['POST'])
def users_submit():
    """Submit a new playlist."""
    user = {
        'username': request.form.get('username'),
        'fullname': request.form.get('fullname')
    }
    users.insert_one(user)
    return redirect(url_for('users_index'))

if __name__ == '__main__':
    app.run(debug=True)
