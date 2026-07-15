class UserManager:


    def __init__(self, database):

        self.database = database

        self.users = [
            "Ali",
            "Admin"
        ]


    def list_users(self):

        return self.users
