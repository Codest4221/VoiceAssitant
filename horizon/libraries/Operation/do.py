from concurrent.futures import thread
from libraries.Hander.sample import cameraHandler
from threading import Thread
# from libraries.Hander.interpreter import


class assistantFunction():
    def __init__(self, databaseHorizon) -> None:
        self.database = databaseHorizon

    def startHander(self):
        camera = cameraHandler(self.database)
        a = Thread(target=camera.main)
        a.start()

    def stopHander(self):
        self.database.cameraCap = 0


class handerFunction():
    def __init__(self, databaseHorizon) -> None:
        self.database = databaseHorizon
