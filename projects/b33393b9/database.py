import sqlite3


class Database:

    def __init__(self, name="shop.db"):
        self.connection = sqlite3.connect(name)


    def execute(self, query, params=()):

        cursor = self.connection.cursor()

        cursor.execute(
            query,
            params
        )

        self.connection.commit()

        return cursor


    def close(self):

        self.connection.close()
