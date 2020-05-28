from DL import DBConn


def fill(password):
    if password.PasswordID == 0:
        return None
    else:
        query = "SELECT p.PasswordID, p.DateCreated, p.DateModified, pd.PasswordType, pd.PasswordName, pd.PasswordUser, pd.PasswordSite, pd.PasswordPassword, pd.PasswordNote " \
                "FROM tPassword p LEFT JOIN tPasswordDetail pd ON p.PasswordDetailID = pd.PasswordDetailID " \
                "WHERE p.UserID = 1"
        result = DBConn.query_return(query)
        if len(result) > 0:
            password.mapper(result)
        else:
            password.PasswordID = 0
        return password
