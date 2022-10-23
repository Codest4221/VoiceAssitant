from database.database import database
import pyttsx3
import speech_recognition as sr
import pyaudio


class Assistant():
    def __init__(self, data: database) -> None:
        self.databaseHorizon = data  # Connecting database
        self.databaseHorizon.engine = pyttsx3.init()
        self.databaseHorizon.engine.setProperty('rate', 125)
        self.databaseHorizon.engine.say(
            f"Hello {self.databaseHorizon.userName}, I am your assistant , Horizon. Let me help you.")
        self.databaseHorizon.engine.runAndWait()

    def main(self) -> None:  # Function for initliazing
        self.databaseHorizon.listener = sr.Recognizer()
        self.databaseHorizon.text: str
        mic = sr.Microphone()
        while True:
            # try:
            with mic as source:
                audio_data = self.databaseHorizon.listener.listen(
                    source)
                # try:
                self.databaseHorizon.text = self.databaseHorizon.listener.recognize_google(
                    audio_data, language="en-in")
                # except:
                # break
            if self.databaseHorizon.shutdownProgram == 1 or self.databaseHorizon.text.lower() == "quit":
                break
            # except:
                #self.databaseHorizon.text = "No Input"
            self.databaseHorizon.commandBuffer.append("weather:[]")