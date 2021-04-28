from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import pyjokes
import wolframalpha

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good night")


class mainT(QThread):
    def _init_(self):
        super(mainT, self)._init_()

    def run(self):
        self.JARVIS()

    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio, language='en-in')
            print(">> ", text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text

    def JARVIS(self):
        wish()
        while True:
            self.query = self.STT()
            if 'good bye' in self.query:
                sys.exit()
            elif 'open google' in self.query:
                webbrowser.open('www.google.co.in')
                speak("opening google")

            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")

            elif 'play music' in self.query:
                speak("playing music from pc")
                self.music_dir = "./music"
                self.musics = os.listdir(self.music_dir)
                os.startfile(os.path.join(self.music_dir, self.musics[0]))

            elif 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'open Linkedin' in query:
                webbrowser.open("Linkedin.com")

            elif 'open Zomato' in query:
                webbrowser.open("Zomato.com")

            elif 'open Google maps' in query:
                webbrowser.open("https://www.google.co.in/maps/@22.6241504,88.4306945,15z")

            elif 'open Uber' in query:
                webbrowser.open("Uber.com")

            elif 'open BigBasket' in query:
                webbrowser.open("BigBasket.com")

            elif 'open Weather' in query:
                webbrowser.open("Weather.com")

            elif 'open ' in query:
                webbrowser.open(".com")

            elif "calculate" in query:

                app_id = "Wolframalpha api id"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)



            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                speak("Sir, the time is {strTime}")

            elif "who i am" in query:
                speak("If you talk then definately your human.")

            elif "why you came to world" in query:
                speak("Thanks to Bros. further It's a secret")


            elif 'joke' in query:
                speak(pyjokes.get_joke())

            elif 'who the heck is' in query:
                person = ('who the heck is', '')
                info = webbrowser.summary(person, 1)
                print(info)
                speak(info)
            elif 'date' in query:
                speak('Sorry, I have a boyfriend')
            elif 'age' in query:
                speak('electrons with double slit')
            elif 'are you single' in query:
                speak('I am in a relationship with wifi')


            elif 'email to divyansh' in query:
                try:
                    speak("What should I say?")
                    content = speak.query()
                    to = "divyanshmathur553@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir. I am not able to send this email")
            else:
                print("Not able to understand the command ")
                speak("Sorry not able to recognize your command")
                break


FROM_MAIN, _ = loadUiType(os.path.join(os.path.dirname(_file_), "./scifi.ui"))


class Main(QMainWindow, FROM_MAIN):
    def _init_(self, parent=None):
        super(Main, self)._init_(parent)
        self.setupUi(self)
        self.setFixedSize(910, 590)
        self.label_2 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
                                 "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/mid.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/UI-design.JPG"))
        self.label_5.setText("<font size=8 color='white'>" + self.ts + "</font>")
        self.label_5.setFont(QFont(QFont('Acens', 8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())
