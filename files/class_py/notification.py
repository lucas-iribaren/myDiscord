from datetime import datetime
from files.class_py.database import Database
from files.class_py.interface import Interface
from files.class_py.message import Message
from files.class_py.user import User

class Notification(Database, Interface):
    def __init__(self, user):
        self.current_time_notif = datetime.now()
        self.user = user
        self.message = Message(self.user)
        self.user = User()
        Database.__init__(self)
        Interface.__init__(self)
        
    def add_notification(self):
        sql = "INSERT INTO notification(text,auteur,heure) VALUES (%s,%s,%s)"
        self.execute_sql(sql, (self.message.input_texts['message'], self.user(self.message.user), self.current_time_notif))
        
    def notification_display(self):
        x_notif = 750
        y_notif = 100
        larg_notif = 150
        high_notif = 50
        self.solid_rect_radius(self.light_grey, x_notif, y_notif, larg_notif, high_notif)
        self.text(15, self.user, self.black, x_notif, y_notif - 30)
        self.text(14, self.current_time_notif, self.white, x_notif + 30, y_notif - 30)
        self.text(13, self.message.input_texts['message'], self.white, x_notif, y_notif + 30)