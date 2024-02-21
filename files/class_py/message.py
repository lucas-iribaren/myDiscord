from files.class_py.database import Database
from datetime import datetime
from files.class_py.interface import Interface

class Message(Database):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.interface = Interface()
        self.current_date_message = datetime.now()
        self.input_texts_message = {'message':''}        
        self.active_input_mes = None 

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
        

    def message_display(self, message, user, x_message, y_message, largeur_message, hauteur_message, radius_message):
        message_text = str(message).strip("()',")
        self.interface.text(15, user, self.interface.red, x_message, y_message - 30)
        self.interface.text(14, self.current_date_message.strftime('%Y-%m-%d %H:%M:%S'), self.interface.white, x_message + 30, y_message - 30)
        self.interface.solid_rect_radius(self.interface.light_grey, x_message, y_message, largeur_message, hauteur_message, radius_message)
        self.interface.text(13, message_text, self.interface.black, x_message + 30, y_message + 30)

        
