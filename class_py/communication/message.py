from datetime import datetime
from class_py.pages.Interface import Interface

class Message(Interface):
    def __init__(self, user):
        super().__init__()
        self.user = user        
        self.current_date_message = datetime.now()
        self.input_texts_message = {'message':''}        
        self.active_input_mes = None
        self.y_offset = 0
                   

    def message_display(self, message, user, x_message, y_message, largeur_message, hauteur_message, radius_message):
        message_text = str(message).strip("()',")
        self.text(15, user, self.red, x_message, y_message + self.y_offset - 30)
        self.text(14, self.current_date_message.strftime('%Y-%m-%d %H:%M:%S'), self.white, x_message + 30, y_message+ self.y_offset - 30)
        self.solid_rect_radius(self.light_grey, x_message, y_message+ self.y_offset, largeur_message, hauteur_message, radius_message)
        self.text(13, message_text, self.black, x_message + 30, y_message+ self.y_offset + 30)
        self.y_offset =+ 100

        
