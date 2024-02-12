from files.class_py.database import Database

class Message(Database):
    def __init__(self, user):         
        Database.__init__(self)
        self.user = user
        
    def add_message(self):
        pass
    
    def delete_message(self):
        pass
        
        
