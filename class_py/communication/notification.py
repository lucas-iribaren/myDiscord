import pygame
from class_py.database.SqlManager import SqlManager
from class_py.pages.Interface import Interface

class Notification(Interface,SqlManager):
    def __init__(self):
        super().__init__()
        self.error_timer = 0
        self.error_duration = 1000
        self.clock = pygame.time.Clock()    

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
            self.solid_rect_radius(self.light_grey, x_notif, y_notif + index * 80, larg_notif, high_notif, radius_notif)
            self.text(17, message_author, self.black, x_notif, y_notif - 30 + index * 80)
            self.text(12, message_time, self.white, x_notif + 30, y_notif - 30 + index * 80)
            self.text(16, message_text, self.white, x_notif, y_notif + 30 + index * 80)
        
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

    