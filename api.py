import flask
from flask import request
from termcolor import colored
import json

from BL.UserBL import UserBL
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


app.run()
