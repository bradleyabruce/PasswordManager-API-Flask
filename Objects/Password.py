class Password:
    def __init__(self):
        # Properties
        self.PasswordID = 0
        self.DateCreated = None
        self.DateModified = None
        self.PasswordType = None
        self.PasswordName = None
        self.PasswordUser = None
        self.PasswordSite = None
        self.PasswordPassword = None
        self.PasswordNote = None

    def mapper(self, result_set):
        for row in result_set:
            if "PasswordID" in row:
                self.PasswordID = row["PasswordID"]
            if "DateCreated" in row:
                self.DateCreated = row["DateCreated"]
            if "DateModified" in row:
                self.DateModified = row["DateModified"]
            if "PasswordType" in row:
                self.PasswordType = row["PasswordType"]
            if "PasswordName" in row:
                self.PasswordName = row["PasswordName"]
            if "PasswordUser" in row:
                self.PasswordUser = row["PasswordUser"]
            if "PasswordSite" in row:
                self.PasswordSite = row["PasswordSite"]
            if "PasswordPassword" in row:
                self.PasswordPassword = row["PasswordPassword"]
            if "PasswordNote" in row:
                self.PasswordNote = row["PasswordNote"]