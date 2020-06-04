import json

from flask import Response

from BL import PasswordBL
from Objects.Exceptions import PasswordLengthTooSmall, PasswordLengthTooLarge
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


def delete(password_id):
    try:
        delete_result = PasswordBL.delete(password_id)
        if delete_result:
            return Response("Success", status=200)
        else:
            return Response("Error", status=503)
    except Exception as e:
        print(e)
        return Response("Error", status=503)


def generate_password(length, include_special_characters, verify_not_pwned):
    try:
        password = PasswordBL.generate_password(int(length), bool(int(include_special_characters)), bool(int(verify_not_pwned)))
        return Response(password, status=200)
    except PasswordLengthTooSmall:
        return Response("Password length too small.", status=200)
    except PasswordLengthTooLarge:
        return Response("Password length too large.", status=200)
    except:
        return Response("Error.", status=503)


def password_pwned_count(password):
    try:
        pwned_count = PasswordBL.password_pwned_count(password)
        return Response(str(pwned_count), status=200)
    except:
        return Response("Error", status=503)


def get_all_user_passwords(user_id, user_password):
    try:
        passwords = PasswordBL.get_all_user_passwords(user_id, user_password)
        return Response(json.dumps([Password.__dict__ for Password in passwords]), status=200, mimetype='application/json')
    except Exception as e:
        print(e)
        return Response("Error", status=503)

