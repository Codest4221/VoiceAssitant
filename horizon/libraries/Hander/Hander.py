from database.database import database
import cv2
import mediapipe
import time
import math
import numpy as np
import screen_brightness_control as sbc
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
mp = mediapipe.solutions.mediapipe.python


class Hander():
    def __init__(self, data: database) -> None:
        mode = False
        maxHands = 2
        trackCon = 0.5
        detectionCon = 0.7
        self.databaseHorizon = data  # Connecting database
        self.databaseHorizon.captureCamera = cv2.VideoCapture(0)
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

    def main(self) -> None:  # Function for initiliazing
        while True:
            ret, self.databaseHorizon.frame = self.databaseHorizon.captureCamera.read()
            cv2.flip(self.databaseHorizon.frame, 0)
            self.findPosition(self.findHands(self.databaseHorizon.frame))
            cv2.imshow(self.databaseHorizon.windowName,
                       self.databaseHorizon.frame)
            if cv2.waitKey(1) == ord("q"):
                self.databaseHorizon.shutdownProgram = 1
                break

    def findHands(self, img, draw=True):
        """Returns an image of the detected hand and draws the landmarks"""
        img = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        img, handlms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        """Returns a list of the lansdmarks corrdinates"""
        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                # print(cx,cy)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(self.databaseHorizon.frame,
                               (cx, cy), 15, (255, 0, 255), 2)

        self.databaseHorizon.point = lmlist
