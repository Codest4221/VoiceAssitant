import socket as soc


class database():
    def __init__(self) -> None:
        # Connection database variable declaration
        self.Port: int
        self.hostName: str
        self.IPaddress: str
        self.server: soc.socket
        self.client: soc.socket
        self.Connection : soc.socket
        self.ConnectionIP : str
        self.message: str
        self.family: soc.AF_INET
        self.protocol: soc.SOCK_STREAM
        self.dataSetCreater()
        #

    def dataSetCreater(self) -> None:
        self.Port = 1000
        self.family: soc.AF_INET
        self.protocol: soc.SOCK_STREAM
        self.hostName = soc.gethostname()
        self.IPaddress = soc.gethostbyname(self.hostName)
        self.message = "Command:None;Arg:None"
