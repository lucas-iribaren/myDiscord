import socket

class Serveur:
    def __init__(self):
        self.host = ''
        self.port = 5566
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.serveur_running = True
        
    def serveur_on(self):
        self.socket.listen(5)
        while self.serveur_running:
            connection, address = self.socket.accept()
            # Traitez la connexion ici
            print("En écoute...")

            connection.close()  # Fermez la connexion à l'intérieur de la boucle pour accepter de nouvelles connexions

        self.socket.close()  # Fermez le socket à l'extérieur de la boucle
