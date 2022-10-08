

# Database
class database():
    # Variable declaration will be handled in the scope of this function
    def __init__(self) -> None:
        self.main()  # Do not change this line and do not delete. The main function calling of database

    def AssistantDatabase(self) -> None:
        self.engine = None
        self.userName = "Mete"

    def ConnectorDatabase(self) -> None:
        pass

    def HanderDatabase(self) -> None:
        self.captureCamera = None
        self.frame = None
        self.windowName = "Window"

    def OperationDatabase(self) -> None:
        pass

    def HorizonDatabase(self) -> None:
        self.shutdownProgram = 0

    def main(self) -> None:
        self.AssistantDatabase()
        self.ConnectorDatabase()
        self.HanderDatabase()
        self.HorizonDatabase()
