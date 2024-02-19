import pygame
from datetime import datetime
from files.class_py.database import Database
from files.class_py.interface import Interface
from files.class_py.message import Message
from files.class_py.user import User

class Notification(Database, Interface):
    def __init__(self, user):
        Database.__init__(self)
        Interface.__init__(self)
        
        self.current_time_notif = datetime.now()
        self.user = user
        self.message = Message(self.user)
        self.clock = pygame.time.Clock()       
        self.error_timer = 0
        self.error_duration = 3500
        self.input_message_users = self.message.input_texts_message['message']        
        
    def add_notification(self):
        sql = "INSERT INTO notification(text, auteur, heure) VALUES (%s, %s, %s)"
        message_text, message_author, message_time = self.message.three_last_messages()[0]
        self.execute_sql(sql, (message_text, message_author, message_time))
        
    def display_notification(self):
        x_notif = 750
        y_notif = 100
        larg_notif = 150
        high_notif = 50
        self.three_last_messages = self.message.three_last_messages()

        for index, notification in enumerate(self.three_last_messages):
            message_text, message_author, message_time = notification

            self.solid_rect_radius(self.light_grey, x_notif, y_notif + index * 80, larg_notif, high_notif)
            self.text(15, message_author, self.black, x_notif, y_notif - 30 + index * 80)
            self.text(14, message_time, self.white, x_notif + 30, y_notif - 30 + index * 80)
            self.text(13, message_text, self.white, x_notif, y_notif + 30 + index * 80)

            if self.error_timer >= self.error_duration:
                self.user = None
                self.current_time_notif = None
                self.input_message_users = None
                self.error_timer = 0
