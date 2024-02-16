from datetime import datetime
from files.class_py.interface import Interface
from files.class_py.database import Database

class Message(Database, Interface):
    def __init__(self, user):         
        Database.__init__(self)
        Interface.__init__(self)
        self.user = user
        self.current_date_message = datetime.now()        
        
    def add_message(self, input_text, auteur, heure, id_channel):
        sql = "INSERT INTO message(text, auteur, heure, id_channel) VALUES (%s, %s, %s, %s);"
        self.execute_sql(sql, (input_text, auteur, self.current_date_message.strftime('%Y-%m-%d %H:%M:%S'), id_channel))
        
    def three_last_messages(self):
        sql = "SELECT text, auteur, heure FROM notification ORDER BY heure DESC LIMIT 3"
        return self.fetch_all(sql, ())
        
    def message_display(self, message, x_message, y_message, largeur_message, hauteur_message, radius_message):
        self.solid_rect_radius(self.light_grey, x_message, y_message, largeur_message, hauteur_message, radius_message)
        self.text(15, self.user, self.black, x_message, y_message - 30)
        self.text(14, self.current_date_message.strftime('%Y-%m-%d %H:%M:%S'), self.white, x_message + 30, y_message - 30)
        self.text(13, message, self.white, x_message + 30, y_message + 30)
