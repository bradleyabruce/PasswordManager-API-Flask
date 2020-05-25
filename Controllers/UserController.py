from BL import UserBL
import json
from flask import Response

from Objects.User import User


def fill(user_id):
    try:
        user = User()
        user.UserID = user_id
        user = UserBL.fill(user)
        if user is not None:
            return Response(json.dumps(user.__dict__), status=200, mimetype='application/json')
        else:
            return Response("Error", status=503)
    except:
        return Response("Error", status=503)


def login(username, password):
    try:
        user = User()
        user.UserName = username
        user.Password = password
        user = UserBL.login(user)
        if user.UserID != 0:
            return Response(json.dumps(user.__dict__), status=200, mimetype='application/json')
        else:
            return Response("Incorrect username or password", status=200)
    except Exception as e:
        return Response("Error - " + str(e), status=503)


def signup(username, password, email, firstname, lastname):
    try:
        user = User()
        user.UserName = username
        user.Password = password
        user.Email = email
        user.FirstName = firstname
        user.LastName = lastname
        user = UserBL.signup(user)
        if user.UserID != 0:
            return Response(json.dumps(user.__dict__), status=200, mimetype='application/json')
        else:
            return Response("Failure signing up", status=200)
    except Exception as e:
        return None


