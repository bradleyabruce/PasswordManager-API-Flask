from BL import UserBL
import json
from flask import Response


def fill(user_id):
    try:
        user = UserBL.UserBL()
        user.UserID = user_id
        user.fill()
        return Response(json.dumps(user.__dict__), status=200, mimetype='application/json')
    except:
        return Response("Error", status=400, mimetype='application/json')
