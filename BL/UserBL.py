import hashlib
import uuid
from DL import DBConn


def fill(user):
    if user.UserID == 0:
        return None
    else:
        query = "SELECT u.Username, u.Email, u.FirstName, u.LastName, u.Password FROM tUsers u WHERE u.UserID = " + str(user.UserID) + ";"
        result = DBConn.query_return(query)
        if len(result) > 0:
            user.mapper(result)
        else:
            user.UserID = 0
        return user


def login(user):
    if user.UserName is not None and user.Password is not None:
        user.Password = hash_password(str(user.Password))
        # The 'BINARY' keyword forces case sensitive searches
        query = "SELECT u.UserID, u.Email, u.FirstName, u.LastName FROM tUsers u WHERE u.Username = '" + user.UserName + "' and u.Password = BINARY '" + user.Password + "';"
        result = DBConn.query_return(query)
        user.mapper(result)
        return user
    else:
        return


def signup(user):
    if user.UserName is not None and user.Password is not None:
        user.Password = hash_password(str(user.Password))
        query = "INSERT INTO tUsers (Username, Password, Email, FirstName, LastName) VALUES ('" + user.UserName + "', '" + user.Password + "', '" + user.Email + "', '" + user.FirstName + "', '" + user.LastName + "');"
        new_id = DBConn.query_insert(query)
        if new_id != 0:
            user.UserID = new_id
            return user
        else:   # return will null ID
            return user


def hash_password(password):
    salt = 'Salt_To_Add_2020'
    salt_bytes = bytearray()
    salt_bytes.extend(salt.encode())
    key = hashlib.pbkdf2_hmac(
        'sha256',  # The hash digest algorithm for HMAC
        password.encode('utf-8'),  # Convert the password to bytes
        salt_bytes,  # Provide the salt
        100000)  # It is recommended to use at least 100,000 iterations of SHA-256
    hashed_password = key.decode("utf-8", "backslashreplace")
    return hashed_password
