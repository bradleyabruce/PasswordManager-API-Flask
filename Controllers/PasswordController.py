import json

from flask import Response

from BL import PasswordBL
from Objects.Password import Password


def fill(password_id):
    try:
        password = Password()
        password.PasswordID = password_id
        password = PasswordBL.fill(password)
        if password is not None:
            return Response(json.dumps(password.__dict__), status=200, mimetype='application/json')
        else:
            return Response("Error", status=503)
    except:
        return Response("Error", status=503)


def insert(password_type, password_name, password_user, password_site, password_password, password_note, password_user_id):
    try:
        password = Password()
        password.PasswordType = password_type
        password.PasswordName = password_name
        password.PasswordUser = password_user
        password.PasswordSite = password_site
        password.PasswordPassword = password_password
        password.PasswordNote = password_note
        password.UserID = password_user_id
        password = PasswordBL.insert(password)
        if password.PasswordID != 0:
            return Response(json.dumps(password.__dict__), status=200, mimetype='application/json')
        else:
            return Response("Error", status=503)
    except Exception as e:
        print(e)
        return Response("Error", status=503)


def generate_password(length, include_special_characters):
    try:
        password = PasswordBL.generate_password(int(length), bool(int(include_special_characters)))
        return Response(password, status=200)
    except Exception as e:
        print(e)
        return Response("Error", status=503)


def password_pwned_count(password):
    try:
        pwned_count = PasswordBL.password_pwned_count(password)
        return Response(str(pwned_count), status=200)
    except:
        return Response("Error", status=503)
