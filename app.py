from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage"""
    msg = "hello!"
    return render_template('home.html', msg = msg)

charities = [
    {'name': 'Moisson Montreal', 'description': 'Food bank', 'projects': []},
     {'name': 'NDG Food depot', 'description': 'Food bank', 'projects': []},
]

@app.route('/charities')
def charities_index():
    return render_template('charities_index.html', charities = charities)

if __name__ == '__main__':
    app.run(debug=True)
