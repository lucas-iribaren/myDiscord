# import mysql.connector

# class Database:
#     def __init__(self, host, user, password, database):
#         self.base = mysql.connector.connect(
#         host = host,
#         user = user,
#         password = password,
#         database = database,
#         )
#         self.cursor = self.base.cursor()

#     def execute_sql(self, query, params=None):
#         self.cursor.execute(query, params or ())
#         self.base.commit()

#     def fetch_all(self, query, params=None):
#         self.cursor.execute(query, params or ())
#         return self.cursor.fetchall()
    
#     def closing_connection(self):
#         self.base.close()
        