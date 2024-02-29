from datetime import datetime
from class_py.pages.Interface import Interface
from class_py.database.SqlManager import SqlManager
import pyaudio
import wave

class Message(Interface, SqlManager):
    def __init__(self, user):
        super().__init__()
        self.user = user        
        self.current_date_message = datetime.now()        
        self.y_offset = 0        
        self.format_sound = pyaudio.paInt16  # Format de l'échantillon
        self.type_cannaux = 1  # Nombre de canaux audio (1 pour mono, 2 pour stéréo)
        self.rate = 44100  # Fréquence d'échantillonnage (en Hz)
        self.chunk = 1024  # Nombre d'échantillons par trame
        self.record = False   
        self.p = pyaudio.PyAudio()
        self.filename = ""  # Variable pour stocker le nom du fichier WAV
        self.frames = []  # Liste pour stocker les trames audio enregistrées
        # Ouverture du flux audio d'entrée (microphone)
        self.stream_in = self.p.open(format=self.format_sound,
                        channels=self.type_cannaux,
                        rate=self.rate,
                        input=True,
                        frames_per_buffer=self.chunk)
        # Ouverture du flux audio de sortie (haut-parleurs)
        self.stream_out = self.p.open(format=self.format_sound,
                            channels=self.type_cannaux,
                            rate=self.rate,
                            output=True,
                            frames_per_buffer=self.chunk)
                
        
    def record_audio(self, filename=None):
        self.frames = []
        self.record = True
        print("Enregistrement audio...")
        if filename:
            self.filename = filename
        # Enregistrement audio
        while self.record:
            data = self.stream_in.read(self.chunk)
            self.frames.append(data)
            

    def stop_recording(self):
        print("Enregistrement arrêté.")
        self.record = False
        # Enregistrer les données audio dans un fichier WAV
        if self.frames and self.filename:
            with wave.open(self.filename, 'wb') as wf:
                wf.setnchannels(self.type_cannaux)
                wf.setsampwidth(self.p.get_sample_size(self.format_sound))
                wf.setframerate(self.rate)
                wf.writeframes(b''.join(self.frames))
                
        
    def play_audio(self, filename=None):
        print("Lecture audio...")
        if filename:  # Si un nom de fichier est fourni, lire à partir du fichier
            wf = wave.open(filename, 'rb')
            stream = self.p.open(format=self.format_sound,
                                channels=self.type_cannaux,
                                rate=self.rate,
                                output=True,
                                frames_per_buffer=self.chunk)
            data = wf.readframes(self.chunk)
            while len(data) > 0:
                stream.write(data)
                data = wf.readframes(self.chunk)
            stream.stop_stream()
            stream.close()
            wf.close()
        else:  # Sinon, lire à partir du flux d'entrée (microphone)
            while True:
                data = self.stream_in.read(self.chunk)
                self.stream_out.write(data)


    def stop_playing(self):
        print("Lecture audio arrêtée.")
        # Arrêter le flux de sortie audio
        self.stream_out.stop_stream()
        # Fermer le flux de sortie audio
        self.stream_out.close()
        # Arrêter l'instance de PyAudio
        self.p.terminate()
    
    def verify_id_category_for_display_messages(self, id_channel, text_active):
        id_channels = self.retrieve_id_channel_message()
        text_chat = self.retrieve_type_channel_for_message(id_channel)
        if id_channel in id_channels and text_active not in text_chat:
            self.channel_active = id_channel   
        
    # For channel messages
    def input_write_user_display(self):
        messages = self.retrieve_messages_by_channel_id(self.channel_active)  # Récupère tous les messages
        if messages:  # Vérifie si des messages sont récupérés
            split_text = []
            line = ""
            for message in messages:
                words = message[1].split(" ")  # Divise le texte du message en mots
                for word in words:
                    if len(line) + len(word) + 1 <= self.W:  # Vérifie si le mot peut être ajouté à la ligne actuelle
                        line += word + " "
                    else:
                        split_text.append(line.strip())  # Ajoute la ligne complète à split_text
                        line = word + " "
                split_text.append(line.strip())  # Ajoute la dernière ligne
            # Maintenant, nous avons une liste de lignes de texte (split_text)
            # Nous allons afficher chaque ligne à une position spécifique sur l'écran
            y_position = 620  # Position verticale initiale
            for ligne in split_text:
                self.text(17, ligne, self.black, 510, y_position)  # Affiche la ligne
                y_position += 15  # Augmente la position verticale pour la prochaine ligne
                
        # # For channel messages
        # def message_server_display(self):
        #     pass

    
    # For private messages
    def message_display(self, message, user, x_message, y_message, largeur_message, hauteur_message, radius_message):
        message_text = str(message).strip("()',")
        self.text(15, user, self.red, x_message, y_message + self.y_offset - 30)
        self.text(14, self.current_date_message.strftime('%Y-%m-%d %H:%M:%S'), self.white, x_message + 30, y_message+ self.y_offset - 30)
        self.solid_rect_radius(self.light_grey, x_message, y_message+ self.y_offset, largeur_message, hauteur_message, radius_message)
        self.text(13, message_text, self.black, x_message + 30, y_message+ self.y_offset + 30)
        self.y_offset += 100
