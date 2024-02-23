import pygame
from files.class_py.database import Database
from files.class_py.interface import Interface
# from files.class_py.message import Message
# from files.class_py.user import User

class Notification(Database):
    def __init__(self):
        super().__init__()
        self.error_timer = 0
        self.error_duration = 1000
        # self.time = datetime.now()
        self.interface = Interface()
        self.clock = pygame.time.Clock()       

    def add_notification(self, three_last_messages):
        for notification in three_last_messages:
            message_text_sql, message_author_sql, message_time_sql = notification

            sql = "INSERT INTO notification(text, auteur, heure) VALUES (%s, %s, %s)"
            self.execute_sql(sql, (message_text_sql, message_author_sql, message_time_sql))

    def display_notification(self, three_last_messages):
        x_notif = 750
        y_notif = 100
        larg_notif = 150
        high_notif = 50
        radius_notif = 5

        for index, notification in enumerate(three_last_messages):
            message_text, message_author, message_time = notification           
            message_time = str(message_time)
            # Dipslay notifications
            self.interface.solid_rect_radius(self.interface.light_grey, x_notif, y_notif + index * 80, larg_notif, high_notif, radius_notif)
            self.interface.text(17, message_author, self.interface.black, x_notif, y_notif - 30 + index * 80)
            self.interface.text(12, message_time, self.interface.white, x_notif + 30, y_notif - 30 + index * 80)
            self.interface.text(16, message_text, self.interface.white, x_notif, y_notif + 30 + index * 80)
        
        # Update timer
        self.error_timer += self.clock.tick()
        if self.error_timer >= self.error_duration:
            # Reset values after timer
            self.error_timer = 0

    def update_after_notif(self, delta_time):
        self.error_timer += delta_time
        if self.error_timer >= self.error_duration:
            self.clear_notifications()
            self.error_timer = 0
            self.message_author = None
            self.message_time = None
            self.message_text = None            

    def clear_notifications(self):
        sql = "DELETE FROM notification"
        self.execute_sql(sql, ())