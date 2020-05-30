from datetime import datetime

from DL import DBConn

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

def insert(password):
    # Detail Entry
    query = "INSERT INTO tPasswordDetail (PasswordType, PasswordName, PasswordUser, PasswordSite, PasswordPassword, PasswordNote) " \
            "VALUES ('" + password.PasswordType + "', '" + password.PasswordName + "', '" + password.PasswordUser + "', '" + password.PasswordSite + "', '" + password.PasswordPassword + "', '" + password.PasswordNote + "');"
    password_detail_id = DBConn.query_insert(query)
    if password_detail_id != 0:
        # Password Entry
        timestamp = datetime.now()
        query = "INSERT INTO tPassword (PasswordDetailID, UserID, DateCreated, DateModified) VALUES (" + str(password_detail_id) + ", " + str(password.UserID) + ", NOW(), NOW());"
        password.PasswordID = DBConn.query_insert(query)
        if password.PasswordID != 0:
            password.DateCreated = str(timestamp)
            password.DateModified = str(timestamp)
            return password
        else:
            return password
    else:  # return will 0 ID
        return password

