from threading import Thread
from datetime import datetime
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
        tur = 1
        while True:
            ret, self.databaseHorizon.frame = self.databaseHorizon.captureCamera.read()
            cv2.imshow(self.databaseHorizon.windowName,
                       self.databaseHorizon.frame)
            if tur == 1:
                functiondir = Thread(target=self.findHands)
                functiondir.start()
                tur = 0
            if cv2.waitKey(1) == ord("q"):
                self.databaseHorizon.shutdownProgram = 1
                break

    def findHands(self, draw=True):
        while True:
            """Returns an image of the detected hand and draws the landmarks"""
            imgRGB = cv2.cvtColor(
                self.databaseHorizon.frame, cv2.COLOR_BGR2RGB)
            self.results = self.hands.process(imgRGB)
            if self.results.multi_hand_landmarks:
                for handlms in self.results.multi_hand_landmarks:
                    if draw:
                        self.mpDraw.draw_landmarks(
                            self.databaseHorizon.frame, handlms, self.mpHands.HAND_CONNECTIONS)
            self.findPosition()
            if self.databaseHorizon.shutdownProgram == 1:
                break

    def findPosition(self, handNo=0, draw=True):
        """Returns a list of the lansdmarks corrdinates"""
        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id,lm)
                h, w, c = self.databaseHorizon.frame.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                # print(cx,cy)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(self.databaseHorizon.frame,
                               (cx, cy), 15, (255, 0, 255), 2)

        self.databaseHorizon.point = lmlist
        print(self.databaseHorizon.point)
