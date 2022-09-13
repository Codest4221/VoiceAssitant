import socket as soc
from database.database import database
import threading as thr


class server():
    def __init__(self, data: database) -> None:
        self.database = data

    def infoDevice(self):
        print(self.database.hostName)
        print(self.database.IPaddress)
        print(self.database.Port)

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

    def recieveMessage(self):
        while True:
            data = self.database.Connection.recv(1024)
            if data.decode("utf-8") == "":
                break
            self.database.messageRecieved = self.database.messageRecieved + \
                data.decode("utf-8")

    def transmitMessage(self, command: str):
        self.database.Connection.sendall(command.encode("utf-8"))


class client():
    def __init__(self, database) -> None:
        self.database = database
