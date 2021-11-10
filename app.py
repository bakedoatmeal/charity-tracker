from flask import Flask, render_template
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for
from  bson.objectid import ObjectId

client = MongoClient()
db = client.Donations
users = db.users
donations = db.donations

app = Flask(__name__)

charities = [
    { 'name': 'SPCA', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'rating': 3, 'projects': [{}, {}], '_id': 1}, 
    { 'name': 'Moisson Montreal', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'rating': 4, 'projects': [{}, {}], '_id': 2},
    { 'name': 'World Wildlife Fund', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'rating': 5, 'projects': [{}, {}], '_id': 3}
]

@app.route('/')
def index():
    """Return homepage"""
    return render_template('users_index.html', users=users.find(), charities=charities)

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
    user_donations = donations.find({'user_id': ObjectId(user_id)})
    return render_template('users_show.html', user = user, donations=user_donations, charities=charities)

#TODO: Add update route for Users
#TODO: Also, can make sub templates for html files

@app.route('/users/<user_id>/delete', methods=['POST'])
def users_delete(user_id):
    users.delete_one({'_id': ObjectId(user_id)})
    return redirect(url_for('users_index'))

@app.route('/users/donations', methods=['POST'])
def donations_new():
    """Submit a new donation"""
    donation = {
        'charity': request.form.get('charity'),
        'amount': request.form.get('amount'),
        'date': request.form.get('date'), 
        'user_id': ObjectId(request.form.get('user_id'))
    }
    donations.insert_one(donation)
    # return redirect(url_for('users_show', user_id=request.form.get('user_id')))
    return redirect(url_for('users_show', user_id=request.form.get('user_id')))

@app.route('/users/donations/<donation_id>', methods=['POST'])
def donations_delete(donation_id):
    donations.delete_one({'_id': ObjectId(donation_id)})
    return redirect(url_for('users_show', user_id=request.form.get('user_id')))

@app.route('/charities/<charity_id>')
def charities_show(charity_id):
    return render_template('charities_show.html', charity = charities[0])

if __name__ == '__main__':
    app.run(debug=True)
