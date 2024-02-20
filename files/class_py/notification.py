import pygame
from datetime import datetime
from files.class_py.database import Database
from files.class_py.interface import Interface
# from files.class_py.message import Message
# from files.class_py.user import User

class Notification(Database):
    def __init__(self):
        super().__init__()
        self.notifications = [] 
        self.error_duration = 3500
        self.time = pygame.time.get_ticks()
        self.interface  = Interface()

    def add_notification(self, text, author, timestamp):
        self.notifications.append((text, author, timestamp))
        # Insérer la notification dans la base de données
        sql = "INSERT INTO notification(text, auteur, heure) VALUES (%s, %s, %s)"
        self.execute_sql(sql, (text, author, timestamp))

    def display_notification(self):
        x_notif = 750
        y_notif = 100
        larg_notif = 150
        high_notif = 50
        radius_notif = 5

        for index, notification in enumerate(self.notifications):
            message_text, message_author, message_time = notification
            message_time = str(message_time)

            # Afficher la notification
            self.interface.solid_rect_radius(self.interface.light_grey, x_notif, y_notif + index * 80, larg_notif, high_notif, radius_notif)
            self.interface.text(15, message_author, self.interface.black, x_notif, y_notif - 30 + index * 80)
            self.interface.text(14, message_time, self.interface.white, x_notif + 30, y_notif - 30 + index * 80)
            self.interface.text(13, message_text, self.interface.white, x_notif, y_notif + 30 + index * 80)

    def update_after_notif(self):
        current_time = pygame.time.get_ticks()
        # Supprimer les notifications après un certain délai
        self.notifications = [(text, author, timestamp) for text, author, timestamp in self.notifications if current_time - timestamp < self.error_duration]


