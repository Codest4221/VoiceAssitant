from database.database import database
import cv2


class Hander():
    def __init__(self, data: database) -> None:
        self.databaseHorizon = data  # Connecting database
        self.databaseHorizon.captureCamera = cv2.VideoCapture(0)

    def main(self) -> None:  # Function for initiliazing
        while True:
            ret, self.databaseHorizon.frame = self.databaseHorizon.captureCamera.read()
            cv2.imshow(self.databaseHorizon.windowName,
                       self.databaseHorizon.frame)
            if cv2.waitKey(10) == ord("q"):
                self.databaseHorizon.shutdownProgram = 1
                break
