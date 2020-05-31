class Password:
    def __init__(self):
        # Properties
        self.PasswordID = 0
        self.DateCreated = None
        self.DateModified = None
        self.UserID = None
        self.PasswordType = None
        self.PasswordName = None
        self.PasswordUser = None
        self.PasswordSite = None
        self.PasswordPassword = None
        self.PasswordNote = None

    def mapper(self, result_set):
        for key, value in result_set.items():
            if "PasswordID" in key:
                self.PasswordID = value
                continue
            if "DateCreated" in key:
                self.DateCreated = str(value)
                continue
            if "DateModified" in key:
                self.DateModified = str(value)
                continue
            if "UserID" in key:
                self.UserID = value
                continue
            if "PasswordType" in key:
                self.PasswordType = value
                continue
            if "PasswordName" in key:
                self.PasswordName = value
                continue
            if "PasswordUser" in key:
                self.PasswordUser = value
                continue
            if "PasswordSite" in key:
                self.PasswordSite = value
                continue
            if "PasswordPassword" in key:
                self.PasswordPassword = value
                continue
            if "PasswordNote" in key:
                self.PasswordNote = value
                continue
