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
