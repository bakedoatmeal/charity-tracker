from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.Donations
charities = db.charities

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage"""
    msg = "hello!"
    return render_template('charities_index.html', charities=charities.find())

@app.route('/charities')
def charities_index():
    return render_template('charities_index.html', charities = charities)

if __name__ == '__main__':
    app.run(debug=True)
