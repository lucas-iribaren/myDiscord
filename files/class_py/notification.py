from datetime import datetime
from files.class_py.message import Message
from files.class_py.database import Database
from files.class_py.interface import Interface
from files.class_py.user import User

class Notification(Database, Interface):
    def __init__(self):
        self.current_time_notif = datetime.now()
        self.message = Message()
        self.user = User()
        Database.__init__(self)
        Interface.__init__(self)
        
    def add_notification(self):
        sql = "INSERT INTO notification(text,auteur,heure) VALUES (%s,%s,%s)"
        self.execute_sql(sql, (self.message.input_texts_message['message'], self.user.recup_user(self.message.user), self.current_time_notif))
        
    def notification_display(self):
        self.solid_rect_radius(self.light_grey, x_message, y_message, largeur_message, hauteur_message, radius_message)
        self.text(15, self.user, self.black, x_message, y_message - 30)
        self.text(14, self.curent_time_message, self.white, x_message + 30, y_message - 30)
        self.text(13, self.input_texts_message['message'], self.white, x_message + 30, y_message + 30)
        
        