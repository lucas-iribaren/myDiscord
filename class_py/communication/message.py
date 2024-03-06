from datetime import datetime
from class_py.pages.Interface import Interface
from class_py.database.SqlManager import SqlManager
import pyaudio, pygame, subprocess
 


class Message(SqlManager, Interface):
    def __init__(self, user):
        SqlManager.__init__(self) 
        Interface.__init__(self)
        self.user = user        
        self.current_date_message = datetime.now()        
        self.y_offset = 0        
        self.format_sound = pyaudio.paInt16  # Format de l'échantillon
        self.type_cannaux = 1  # Nombre de canaux audio (1 pour mono, 2 pour stéréo)
        self.rate = 44100  # Fréquence d'échantillonnage (en Hz)
        self.chunk = 1024  # Nombre d'échantillons par trame
        self.record = False   
        self.p = pyaudio.PyAudio()
        self.filename = ""  # Variable pour stocker le nom du fichier MP3
        self.frames = []  # Liste pour stocker les trames audio enregistrées
        self.id_channel_for_mes = 0
        self.mes = []  # Initialisez l'attribut mes avec une liste vide
        self.font = pygame.font.Font('font/helvetica_neue_regular.otf', 16)

                
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
        # Enregistrer les données audio dans un fichier MP3
        if self.frames and self.filename:
            with open(self.filename, 'wb') as f:
                subprocess.run(["ffmpeg", "-f", "s16le", "-ar", "44100", "-ac", "1", "-i", "-", "-y", "-codec:a", "libmp3lame", self.filename], input=b''.join(self.frames))
                
        
    def play_audio(self, filename=None):
        print("Lecture audio...")
        if filename:  # Si un nom de fichier est fourni, lire à partir du fichier
            subprocess.run(["ffplay", filename])
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
        
    
    def verify_id_category_for_display_messages(self, id_channel):
        id_channels = self.retrieve_id_channel_message()
        if id_channel in id_channels:
            self.channel_active = id_channel
            self.mes = self.retrieve_messages_by_channel_id(self.channel_active)          
        
    
    # For channels messages    
    def display_writed_channel(self):
        texte = ""
        for tup in self.mes:
            # Concatenate the elements of the tuple with spaces between them
            texte += " \n".join(str(item) for item in tup) + "\n\n"            
            text_width, text_height = self.font.render(texte, True, self.light_grey).get_size()        
        # Set the result as the text of a label
            # self.solid_rect_radius(self.light_grey, 300, 150, text_width, text_height + 50,3 )
            self.solid_rect_radius(self.light_grey, 300, 150, text_width, text_height,3)
            self.text_jump_line(16, texte, self.red, 300, 150)   
            
            
    def message_display_channel(self, message, user, x_message, y_message):
        message_text = str(message).strip("()',")
        self.text(15, user, self.red, x_message, y_message + self.y_offset - 30)
        self.text(14, self.current_date_message.strftime('%Y-%m-%d %H:%M:%S'), self.white, x_message + 30, y_message+ self.y_offset - 30)        
        self.text_jump_line(13, message_text, self.black, x_message + 30, y_message + 30)
        message_text = ""
        self.text_jump_line(13, message_text, self.black, x_message + 30, y_message + 30)       
                        
    
    # For private messages
    def message_display(self, message, user, x_message, y_message, largeur_message, hauteur_message, radius_message):
        message_text = str(message).strip("()',")
        self.text(15, user, self.red, x_message, y_message + self.y_offset - 30)
        self.text(14, self.current_date_message.strftime('%Y-%m-%d %H:%M:%S'), self.white, x_message + 30, y_message+ self.y_offset - 30)
        self.solid_rect_radius(self.light_grey, x_message, y_message+ self.y_offset, largeur_message, hauteur_message, radius_message)
        self.text_jump_line(13, message_text, self.black, x_message + 30, y_message+ self.y_offset + 30)
        self.y_offset += 100
        
