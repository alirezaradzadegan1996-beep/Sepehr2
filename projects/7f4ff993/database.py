import sqlite3


class Database:

    def __init__(self, db="shop.db"):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def create(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER
        )
        """)
        self.conn.commit()
