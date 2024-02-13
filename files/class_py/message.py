from files.class_py.database import Database

class Message(Database):
    def __init__(self, user):         
        Database.__init__(self)
        self.user = user
        
    def add_message(self, input_text, auteur, heure, id_channel):
        sql = "INSERT INTO message(text,auteur,heure,id_channel) VALUES (%s,%s,%s,%s);"
        self.execute_sql(sql, (input_text, auteur, heure, id_channel))
    
    def delete_message(self):
        pass
        
        
