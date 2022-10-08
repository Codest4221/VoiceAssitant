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
        self.databaseHorizon.listener = sr.Recognizer()

    def main(self) -> None:  # Function for initliazing
        self.databaseHorizon.text: str
        while True:
            with sr.Microphone(1) as source:
                self.databaseHorizon.listener.adjust_for_ambient_noise(
                    source, 1)
                self.databaseHorizon.text = self.databaseHorizon.listener.listen(
                    source)
                self.databaseHorizon.text = + \
                    self.databaseHorizon.listener.recognize_google(
                        self.databaseHorizon.text, language='hi-IN')
            if self.databaseHorizon.shutdownProgram == 1 or self.databaseHorizon.text.lower() == "quit":
                break
