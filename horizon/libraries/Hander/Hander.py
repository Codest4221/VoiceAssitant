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


    def __init__(self,mode = False, maxHands=2,detectionCon=0.7,trackCon = 0.5):
        self.__version__ = 1.0
        self.__creator__ = "Codest Team"
        self.__website__ = "http://codest.org/"
        self.mode = mode 
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img,draw = True):
        """Returns an image of the detected hand and draws the landmarks"""
        img = cv2.flip(img,1)
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks: 
            for handlms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handlms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo = 0, draw = True):
        """Returns a list of the lansdmarks corrdinates"""
        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myHand.landmark):
                #print(id,lm)
                h, w, c = img.shape 
                cx , cy = int(lm.x*w) , int(lm.y*h)
                #print(cx,cy)
                lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),15,(255,0,255),2)

        return lmlist
######################################### 2nd file
    # I/O No.1 Volume Control
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
                        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volRange = volume.GetVolumeRange()
    def volControl(self,indexPoint,thumbPoint):
        self.minVol = self.volRange[0]
        self.maxVol = self.volRange[1]
        self.length = math.hypot(indexPoint[0]-thumbPoint[0],indexPoint[1]-thumbPoint[1])
        self.vol = np.interp(self.length, [20, 220], [self.minVol, self.maxVol])
        output = self.volume.SetMasterVolumeLevel(self.vol, None)
        return output

    #I/O No.2 Brightness Control
    def brightness_Control(self,indexPoint,thumbPoint):
        self.length = math.hypot(indexPoint[0]-thumbPoint[0],indexPoint[1]-thumbPoint[1])
        self.level = np.interp(self.length, [20, 220], [0,100])
        return sbc.set_brightness(self.level) 