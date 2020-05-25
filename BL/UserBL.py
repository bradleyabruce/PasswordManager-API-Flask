import hashlib
import uuid

import bcrypt as bcrypt

from DL import DBConn


def fill(user):
    if user.UserID == 0:
        return None
    else:
        query = "SELECT u.Username, u.Email, u.FirstName, u.LastName, u.Password FROM tUsers u WHERE u.UserID = " + str(user.UserID) + ";"
        result = DBConn.query_return(query)
        user.mapper(result)
        return user


def login(user):
    if user.UserName is not None and user.Password is not None:
        # user.password = hash_password(str(user.Password))
        # The 'BINARY' keyword forces case sensitive searches
        query = "SELECT u.UserID, u.Email, u.FirstName, u.LastName FROM tUsers u WHERE u.Username = '" + user.UserName + "' and u.Password = BINARY '" + user.Password + "';"
        result = DBConn.query_return(query)
        user.mapper(result)
        return user
    else:
        return


def signup(user):
    if user.UserName is not None and user.Password is not None:
        # user.password = hash_password(str(user.Password))
        query = "INSERT INTO tUsers (Username, Password, Email, FirstName, LastName) VALUES ('" + user.UserName + "', '" + user.Password + "', '" + user.Email + "', '" + user.FirstName + "', '" + user.LastName + "');"
        new_id = DBConn.query_insert(query)
        if new_id != 0:
            user.UserID = new_id
            return user
        else:   # return will null ID
            return user


def hash_password(password):
    password.encode('utf-8')
    salt = uuid.uuid4().hex
    salt.encode('utf-8')
    hashed_password = hashlib.sha512(password + salt).hexdigest()
    return hashed_password


