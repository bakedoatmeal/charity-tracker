from flask import Flask, render_template
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for
from  bson.objectid import ObjectId

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

@app.route('/users/<user_id>')
def users_show(user_id):
    """Show a single user's information."""
    user = users.find_one({'_id': ObjectId(user_id)})
    return render_template('users_show.html', user = user)

#TODO: Add update route for Users
#TODO: Also, can make sub templates for html files

@app.route('/users/<user_id>/delete', methods=['POST'])
def users_delete(user_id):
    users.delete_one({'_id': ObjectId(user_id)})
    return redirect(url_for('users_index'))

if __name__ == '__main__':
    app.run(debug=True)
