from database.database import database


class Do():
    def __init__(self, data: database) -> None:
        self.databaseHorizon = data
