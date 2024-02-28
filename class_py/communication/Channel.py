from class_py.database.SqlManager import SqlManager
from class_py.pages.Interface import Interface

class Channel(Interface, SqlManager):
    def __init__(self):
        super().__init__()
        self.all_channel = self.get_channels()
        self.all_category = self.get_category()
        
    def display_channel_and_category(self):
        for index, username in enumerate(self.all_channel):
                y_position = 30 + index * 30
            
    
    
        