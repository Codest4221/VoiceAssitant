from database.database import database
import pyttsx3


class Assistant():
    def __init__(self, data: database) -> None:
        self.databaseHorizon = data  # Connecting database
        self.databaseHorizon.engine = pyttsx3.init()
        self.databaseHorizon.engine.setProperty('rate', 125)
        self.databaseHorizon.engine.say(
            f"Hello {self.databaseHorizon.userName}, I am your assistant , Horizon. Let me help you.")
        self.databaseHorizon.engine.runAndWait()

    def main(self) -> None:  # Function for initliazing
        pass
