import socket as soc


class database():
    def __init__(self) -> None:
        # Connection database variable declaration
        # Constant configuration
        self.Port: int
        self.hostName: str
        self.IPaddress: str
        self.family: soc.AF_INET
        self.protocol: soc.SOCK_STREAM
        #
        # Server object dataset
        self.server: soc.socket
        #

        # Connected client dataset
        self.Connection: soc.socket
        self.ConnectionIP: str
        self.messageRecieved: str
        #

        # Configuration function
        self.dataSetCreater()
        #

    def dataSetCreater(self) -> None:
        self.Port = 1000
        self.family: soc.AF_INET
        self.protocol: soc.SOCK_STREAM
        self.hostName = soc.gethostname()
        self.IPaddress = soc.gethostbyname(self.hostName)
