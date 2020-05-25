from DL import DBConn


class UserBL:
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
            self.UserName = row["Username"]
            self.Password = row["Password"]
            self.Email = row["Email"]
            self.FirstName = row["FirstName"]
            self.LastName = row["LastName"]

    @staticmethod
    def query_return(query):
        conn = DBConn.return_connection()
        cursor = conn.cursor(buffered=True, dictionary=True)
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        finally:
            cursor.close()
            conn.close()

    def fill(self):
        if self.UserID == 0:
            return None
        else:
            query = "SELECT u.Username, u.Email, u.FirstName, u.LastName, u.Password FROM tUsers u WHERE u.UserID = " + str(
                self.UserID)
            result = self.query_return(query)
            self.mapper(result)
