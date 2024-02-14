import socket

class Client:
    def __init__(self):
        
        self.host = "localhost"  # Adresse du serveur
        self.port = 5566  # Port utilisé par le serveur
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def client_connected(self):
        try:
            self.socket.connect((self.host, self.port))
            print("Client connecté au serveur")
        except Exception as e:
            print("La connexion au serveur a échoué:", e)
        finally:
            self.socket.close()
