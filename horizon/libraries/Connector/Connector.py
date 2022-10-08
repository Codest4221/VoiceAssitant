from database.database import database


class Connector():
    def __init__(self, data: database) -> None:
        self.databaseHorizon = data

    def main(self) -> None:
        pass
