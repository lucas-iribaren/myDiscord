from files.class_py.database import Database

class User(Database):
    def __init__(self):
        Database.__init__(self)
        
    def add_user(self, pseudo, mail, password, id_categorie):
        sql = "INSERT INTO user (pseudo, mail, password, id_role) VALUES (%s, %s, %s, %s);"
        self.execute_sql(sql, (pseudo, mail, password, id_categorie))
        self.closing_connection()
        
    def update_user(self, user_id, new_pseudo, new_mail, new_password, new_id_categorie):
        sql = "UPDATE user SET pseudo = %s, mail = %s, password = %s, id_role = %s WHERE id = %s;"
        self.execute_sql(sql, (new_pseudo, new_mail, new_password, new_id_categorie, user_id))
        self.closing_connection()
    
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
        
    
