class User:
    def __init__(self):
        # Properties
        self.UserID = 0
        self.UserName = None
        self.Email = None
        self.FirstName = None
        self.LastName = None
        self.Password = None

    def mapper(self, result_set):
        for row in result_set:
            if "UserID" in row:
                self.UserID = row["UserID"]
            if "Username" in row:
                self.UserName = row["Username"]
            if "Password" in row:
                self.Password = row["Password"]
            if "Email" in row:
                self.Email = row["Email"]
            if "FirstName" in row:
                self.FirstName = row["FirstName"]
            if "LastName" in row:
                self.LastName = row["LastName"]
