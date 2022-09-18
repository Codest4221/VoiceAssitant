import num2words
from googlesearch import search
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
from urllib.request import urlopen
import sys
import cv2 
import pytesseract
from PIL import Image
import time
#import threading as thr
from sys import platform
from helper import *
from youtube import youtube
from selenium import webdriver
import chromedriver_autoinstaller as chromedriver
chromedriver.install()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

class Horizon:
    def __init__(self) -> None:
        if platform == "linux" or platform == "linux2":
            self.chrome_path = '/usr/bin/google-chrome'

        elif platform == "darwin":
            self.chrome_path = 'open -a /Applications/Google\ Chrome.app'

        elif platform == "win32":
            self.chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        else:
            print('Unsupported OS')
            exit(1)
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(self.chrome_path)
        )
    def saver():
        fileth = open("recognized.txt", "w+")
        fileth.write("")
        fileth.close()

    def wishMe(self) -> None:
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning SIR")
        elif hour >= 12 and hour < 18:
            speak("Good Afternoon SIR")

        else:
            speak('Good Evening SIR')

        #weather()
        speak('I am Horizon. Please tell me how can I help you?')

    def execute_query(self, query):
        # TODO: make this more concise
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif "weather" in query:
            fox = webdriver.Chrome()
            fox.get('https://weather.com/tr-TR/kisisel/bugun/l/TUXX0002:1:TU?Goto=Redirected')

            time.sleep(1)

            element = fox.find_element_by_id('WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034')
            location = element.location
            size = element.size
            fox.save_screenshot('weather_mn.png')
            fox.quit()

			# trim selenium screen shot inspired from stackoverlow
			# http://stackoverflow.com/questions/15018372/how-to-take-partial-screenshot-with-selenium-webdriver-in-python

            im = Image.open('weather_mn.png')

            left = location['x']
            top = location['y']
			# dimensions added to capture just widget area
            right = location['x'] + 500
            bottom = location['y'] + 200

            im = im.crop((left, top, right, bottom)) # defines crop points
            im.save("weather_croped.png", "PNG")

            image = cv2.imread("weather_croped.png")
            grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            grayscale = cv2.imwrite("weather_cropedBW.png",grayscale)


			# Import required packages

			# Mention the installed location of Tesseract-OCR in your system
            pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract'

			# Read image from which text needs to be extracted
            img = cv2.imread("weather_cropedBW.png")

			# Preprocessing the image starts

			# Convert the image to gray scale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

			# Performing OTSU threshold
            ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

			# Specify structure shape and kernel size.
			# Kernel size increases or decreases the area
			# of the rectangle to be detected.
			# A smaller value like (10, 10) will detect
			# each word instead of a sentence.
            rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

			# Applying dilation on the threshold image
            dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

			# Finding contours
            contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
															cv2.CHAIN_APPROX_NONE)

			# Creating a copy of image
            im2 = img.copy()

			
			# A text file is created and flushed
			
			

			# Looping through the identified contours
			# Then rectangular part is cropped and passed on
			# to pytesseract for extracting text from it
			# Extracted text is then written into the text file
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
				
				# Drawing a rectangle on copied image
                rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
				
				# Cropping the text block for giving input to OCR
                cropped = im2[y:y + h, x:x + w]
				
				# Open the file in append mode
                file = open("recognized.txt", "a")
				
				# Apply OCR on the cropped image
                text = pytesseract.image_to_string(cropped)
				
				# Appending the text into file
                file.write(text)
                file.write("\n")
				
				# Close the file
                file.close

            #a = thr.Thread(target=saver)
            #a.start()
			#file = open("recognized.txt", "w+")
			#file.write("")
			#file.close()
            file = open("recognized.txt","r")
            liste = file.readlines()
            line = liste[2]
            line = line[0:2]
            line ="The weather is " + num2words.num2words(int(line)).replace("-", " ") + " degree"
            speak(line)
            file.close()

        elif 'horizon are you there' in query:
            speak("Yes Sir, at your service")
        elif 'horizon who made you' in query:
            speak("Codest")

        elif 'open youtube' in query:

            webbrowser.get('chrome').open_new_tab('https://youtube.com')
            
        elif 'open amazon' in query:
            webbrowser.get('chrome').open_new_tab('https://amazon.com')

        elif 'battery' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'open google' in query:
            webbrowser.get('chrome').open_new_tab('https://google.com')

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open_new_tab('https://stackoverflow.com')

        elif 'play music' in query:
            os.startfile("Müzikler")

        elif 'search youtube' in query:
            speak('What you want to search on Youtube?')
            youtube(takeCommand())
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strTime}')

        elif 'search' in query:
            speak('What do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get('chrome').open_new_tab(
                url)
            speak('Here is What I found for' + search)

        elif 'location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)

        elif 'your master' in query:
            if platform == "win32" or "darwin":
                speak('Gaurav is my master. He created me couple of days ago')
            elif platform == "linux" or platform == "linux2":
                name = getpass.getuser()
                speak(name, 'is my master. He is running me right now')

        elif 'your name' in query:
            speak('My name is Horizon')
        elif 'who made you' in query:
            speak('I was created by my AI master in 2021')
            
        elif 'stands for' in query:
            speak('J.A.R.V.I.S stands for JUST A RATHER VERY INTELLIGENT SYSTEM')
        elif 'open code' in query:
            if platform == "win32":
                os.startfile(
                    "C:\\Users\\gs935\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('code .')

        elif 'shutdown' in query:
            if platform == "win32":
                os.system('shutdown /p /f')
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('poweroff')

        elif 'cpu' in query:
            cpu()
        elif 'your friend' in query:
            speak('My friends are Google assisstant alexa and siri')

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'github' in query:
            webbrowser.get('chrome').open_new_tab(
                'https://github.com/FurkanCan-eee')

        elif "take note" in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'sleep' in query:
            sys.exit()

        elif 'dictionary' or "translate" in query:
            speak('What you want to search in your intelligent dictionary?')
            translate(takeCommand())



if __name__ == '__main__':
    bot_ = Horizon()
    bot_.wishMe()
    while True:
        query = takeCommand().lower()
        bot_.execute_query(query)
