from class_py.database.Database import Database

class SqlManager(Database):
    def __init__(self):
        Database.__init__(self)        
        
    def add_user(self, pseudo, mail, password, id_category):
        sql = "INSERT INTO user (pseudo, mail, password, id_role) VALUES (%s, %s, %s, %s);"
        self.execute_sql(sql, (pseudo, mail, password, id_category))
        self.closing_connection()
        
    def update_user(self, user_id, new_pseudo, new_mail, new_password, new_id_category):
        sql = "UPDATE user SET pseudo = %s, mail = %s, password = %s, id_role = %s WHERE id = %s;"
        self.execute_sql(sql, (new_pseudo, new_mail, new_password, new_id_category, user_id))
        self.closing_connection()
        
    def recup_info_user(self):
        sql = "SELECT * FROM user"
        all_user = self.fetch_all(sql, ())
        for user in all_user:
            return user[0],user[1],user[2],user[3],user[4]   
    
    def role_upgrade(self, user_id, new_id_role):
        sql = "UPDATE user SET id_role = %s WHERE id = %s"
        self.execute_sql(sql, (new_id_role, user_id))
        self.closing_connection()   
    
    def display_user(self):
        sql = "SELECT pseudo FROM user"
        self.fetch_all(sql,())

    def delete_user(self, user_id):
        sql = "DELETE FROM user WHERE id = %s;"
        self.execute_sql(sql, (user_id,))
        self.closing_connection()
        
    def add_message(self, input_text, auteur, heure, id_channel):
        sql = "INSERT INTO message(text, auteur, heure, id_channel) VALUES (%s, %s, %s, %s);"
        self.execute_sql(sql, (input_text, auteur, heure, id_channel))
        print(input_text)

    def three_last_messages(self):
        sql = "SELECT text, auteur, heure FROM message ORDER BY heure DESC LIMIT 3"
        return self.fetch_all(sql, ())
    
    def last_message(self):
        sql = "SELECT text FROM message ORDER BY heure DESC LIMIT 1"
        return self.fetch_one(sql, ())
        
    
