from mimetypes import init
import cv2


class cameraHandler():
    def __init__(self, databaseHorizon) -> None:
        self.database = databaseHorizon

    def main(self):
        cv2.waitKey(1000)
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow("window", frame)
            if cv2.waitKey(5) == ord("q") or self.database.cameraCap == 0:
                break
        cap.release()
