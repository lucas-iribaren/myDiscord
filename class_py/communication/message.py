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
        self.format_sound = pyaudio.paInt16  # Sample format
        self.type_channels = 1  # Number of audio channels (1 for mono, 2 for stereo)
        self.rate = 44100  # Sample rate (in Hz)
        self.chunk = 1024  # Number of samples per chunk
        self.record = False   
        self.p = pyaudio.PyAudio()
        self.filename = ""  # Variable to store the MP3 file name
        self.frames = []  # List to store recorded audio frames
        self.id_channel_for_mes = 0
        self.mes_text = []  
        self.mes_user = []
        self.mes_date = []
        self.font = pygame.font.Font('font/helvetica_neue_regular.otf', 16)

                
        # Open input audio stream (microphone)
        self.stream_in = self.p.open(format=self.format_sound,
                        channels=self.type_channels,
                        rate=self.rate,
                        input=True,
                        frames_per_buffer=self.chunk)
        # Open output audio stream (speakers)
        self.stream_out = self.p.open(format=self.format_sound,
                            channels=self.type_channels,
                            rate=self.rate,
                            output=True,
                            frames_per_buffer=self.chunk)
                
        
    def record_audio(self, filename=None):
        self.frames = []
        self.record = True
        if filename:
            self.filename = filename
        # Audio recording
        while self.record:
            data = self.stream_in.read(self.chunk)
            self.frames.append(data)
            

    def stop_recording(self):
        self.record = False
        # Save audio data to an MP3 file
        if self.frames and self.filename:
            with open(self.filename, 'wb') as f:
                subprocess.run(["ffmpeg", "-f", "s16le", "-ar", "44100", "-ac", "1", "-i", "-", "-y", "-codec:a", "libmp3lame", self.filename], input=b''.join(self.frames))
                
        
    def play_audio(self, filename=None):
        if filename:  # If a file name is provided, play from the file
            subprocess.run(["ffplay", filename])
        else:  # Otherwise, play from the input stream (microphone)
            while True:
                data = self.stream_in.read(self.chunk)
                self.stream_out.write(data)


    def stop_playing(self):
        # Stop the audio output stream
        self.stream_out.stop_stream()
        # Close the audio output stream
        self.stream_out.close()
        # Terminate the PyAudio instance
        self.p.terminate()
                
    
    def verify_id_category_for_display_messages(self, id_channel):
        id_channels = self.retrieve_id_channel_message()
        if id_channel in id_channels:
            self.channel_active = id_channel
            self.mes_text = self.retrieve_messages_text_by_channel_id(self.channel_active)
            self.mes_user = self.retrieve_messages_user_by_channel_id(self.channel_active)  
            self.mes_date = self.retrieve_messages_date_by_channel_id(self.channel_active)  
    
    # For channels messages    
    def display_writed_message_channel(self):
        text = ""
        user = ""
        date = ""

        for i in self.mes_user:    
            user += "\n".join(str(item) for item in i) + "\n\n"
            self.text_jump_line(18, user, self.black,305, 45)    

        for j in self.mes_date:
            date += "\n".join(str(item) for item in j) + "\n\n"
            self.text_jump_line(18, date, self.soft_black,350, 45)    

        for tup in self.mes_text:            
            # Concatenate the elements of the tuple with spaces between them
            text += " \n".join(str(item) for item in tup) + "\n\n"
            self.text_jump_line(18, text, self.white, 305, 65)
