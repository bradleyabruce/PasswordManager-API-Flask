import hashlib
import string
from datetime import datetime
import random

import requests

from DL import DBConn
from Objects.Exceptions import PasswordLengthTooSmall, PasswordLengthTooLarge

"""
Fill Method.
We do NOT want this method accessible from outside the API
"""
def fill(password):
    if password.PasswordID == 0:
        return None
    else:
        query = "SELECT p.PasswordID, p.DateCreated, p.DateModified, p.UserID, pd.PasswordType, pd.PasswordName, pd.PasswordUser, pd.PasswordSite, pd.PasswordPassword, pd.PasswordNote " \
                "FROM tPassword p LEFT JOIN tPasswordDetail pd ON p.PasswordDetailID = pd.PasswordDetailID " \
                "WHERE p.PasswordID = " + password.PasswordID + ";"
        result = DBConn.query_return(query)
        if len(result) > 0:
            password.mapper(result)
        else:
            password.PasswordID = 0
        return password

"""
Insert Method
"""
def insert(password):
    # Detail Entry
    query = "INSERT INTO tPasswordDetail (PasswordType, PasswordName, PasswordUser, PasswordSite, PasswordPassword, PasswordNote) " \
            "VALUES ('" + password.PasswordType + "', '" + password.PasswordName + "', '" + password.PasswordUser + "', '" + password.PasswordSite + "', '" + password.PasswordPassword + "', '" + password.PasswordNote + "');"
    password_detail_id = DBConn.query_insert(query)
    if password_detail_id != 0:
        # Password Entry
        timestamp = str(datetime.now())
        query = "INSERT INTO tPassword (PasswordDetailID, UserID, DateCreated, DateModified) VALUES (" + str(password_detail_id) + ", " + str(password.UserID) + ", NOW(), NOW());"
        password.PasswordID = DBConn.query_insert(query)
        if password.PasswordID != 0:
            password.DateCreated = timestamp
            password.DateModified = timestamp
            return password
        else:
            return password
    else:  # return will 0 ID
        return password

"""
Generate Password
"""
def generate_password(length, include_special_characters, verify_not_pwned):
    if length < 4:
        raise PasswordLengthTooSmall
    if length > 24:
        raise PasswordLengthTooLarge

    characters = string.ascii_letters + string.digits
    if include_special_characters:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))

    # if verify_not_pwned:
    #    if password_pwned_count(password) > 0:

    return password


def password_pwned_count(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    head, tail = sha1_password[:5], sha1_password[5:]
    url = 'https://api.pwnedpasswords.com/range/' + head
    res = requests.get(url)
    if not res.ok:
        raise RuntimeError('Error fetching "{}": {}'.format(
            url, res.status_code))
    hashes = (line.split(':') for line in res.text.splitlines())
    count = next((int(count) for t, count in hashes if t == tail), 0)
    return count
