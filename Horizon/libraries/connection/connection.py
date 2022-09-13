import socket as soc
from database.database import database
import threading as thr


class server():
    def __init__(self, data: database) -> None:
        self.database = data

    def initializeServer(self):
        self.database.server = soc.socket(
            self.database.family, self.database.protocol)
        self.database.server.bind(
            (self.database.IPaddress, self.database.Port))
        self.database.server.listen()

    def acceptServer(self):
        self.Connection, self.ConnectionIP = self.database.server.accept()

    def acceptServerThread(self):
        x = thr.Thread(target=self.acceptServer)
        x.start()


class client():
    def __init__(self, database) -> None:
        self.database = database
