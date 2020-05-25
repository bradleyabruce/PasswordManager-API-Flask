import flask
from flask import request
from termcolor import colored
import json
from Controllers import UserController

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "Hello World"


# User Functions
@app.route('/api/v1.0/User/fill', methods=['POST'])
def user_fill():
    json_data = request.get_json()
    return UserController.fill(json_data['user_id'])
@app.route('/api/v1.0/User/login', methods=['POST'])
def user_login():
    json_data = request.get_json()
    return UserController.login(json_data['username'], json_data['password'])
@app.route('/api/v1.0/User/signup', methods=['POST'])
def user_signup():
    json_data = request.get_json()
    return UserController.signup(json_data['username'], json_data['password'], json_data['email'], json_data['firstname'], json_data['lastname'])


if __name__ == '__main__':
    app.run(host="localhost", port=8092, debug=False)
