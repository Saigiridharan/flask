from flask import Flask
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/about')
def about():
    return 'About Page'
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route('/api/data')
def get_data():
    return jsonify({'key': 'value'})