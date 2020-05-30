import hashlib
import random
from DL import DBConn
from Objects.Exceptions import EmailUnavailableException, UsernameUnavailableException

"""
Fill Method.
We do NOT want this method accessible from outside the API
"""
def fill(user):
    if user.UserID == 0:
        return None
    else:
        query = "SELECT u.Username, u.Salt, u.Email, u.FirstName, u.LastName, u.Password FROM tUsers u WHERE u.UserID = " + str(
            user.UserID) + ";"
        result = DBConn.query_return(query)
        if len(result) > 0:
            user.mapper(result)
        else:
            user.UserID = 0
        return user

"""
Login and Sign up Functions
"""
def login(user):
    if user.UserName is not None and user.Password is not None:
        user.Password = get_hashed_password(user.UserName, user.Password)
        # The 'BINARY' keyword forces case sensitive searches
        query = "SELECT u.UserID, u.Salt, u.Email, u.FirstName, u.LastName FROM tUsers u WHERE u.Username = '" + user.UserName + "' and u.Password = BINARY '" + user.Password + "';"
        result = DBConn.query_return(query)
        user.mapper(result)
        return user
    else:
        return


def signup(user):
    if not verify_unused_email(user.Email):
        raise EmailUnavailableException()
    if not verify_unused_username(user.UserName):
        raise UsernameUnavailableException()

    user.Password, user.Salt = hash_password(str(user.Password))
    query = "INSERT INTO tUsers (Username, Password, Salt, Email, FirstName, LastName) VALUES ('" + user.UserName + "', '" + user.Password + "', '" + user.Salt + "', '" + user.Email + "', '" + user.FirstName + "', '" + user.LastName + "');"
    new_id = DBConn.query_insert(query)
    if new_id != 0:
        user.UserID = new_id
        return user
    else:  # return will 0 ID
        return user


def hash_password(password):
    # Generate random salt
    rand_salt_int = str(random.randint(100000, 1000000000))
    rand_salt_array = rand_salt_int.encode("utf-8", "ignore")

    # Hash user's password with user's salt array
    key = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), rand_salt_array, 100000)
    hashed_password = key.decode("utf-8", "ignore")
    return hashed_password, rand_salt_int


def get_hashed_password(username, password):
    salt = get_user_salt(username)
    key = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    hashed_password = key.decode("utf-8", "ignore")
    return hashed_password


def get_user_salt(username):
    query = "SELECT u.Salt FROM tUsers u WHERE u.Username = '" + username + "';"
    result = DBConn.query_return(query)
    if len(result) == 1:
        salt = next(iter(result))["Salt"]
        # Encode back into byte array
        salt = salt.encode("utf-8", "ignore")
        return salt


def verify_unused_username(username):
    query = "SELECT u.Username FROM tUsers u WHERE u.Username = '" + username + "';"
    result = DBConn.query_return(query)
    if len(result) > 0:
        return False
    else:
        return True


def verify_unused_email(email):
    query = "SELECT u.Email FROM tUsers u WHERE u.Email = '" + email + "';"
    result = DBConn.query_return(query)
    if len(result) > 0:
        return False
    else:
        return True
"""
End Login and Signup Functions
"""