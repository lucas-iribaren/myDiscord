import mysql.connector

class Database:
    def __init__(self):
        self.base = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "azerty",
        database = "mydiscord",
        )
        self.cursor = self.base.cursor()

    def execute_sql(self, query, params):
        self.cursor.execute(query, params or ())
        self.base.commit()
        self.cursor.close()

    def fetch_all(self, query, params):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()
    
    
    def fetch_one(self, query, params):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()
    
    def closing_connection(self):
        self.base.close()
        