import datetime
import os
import random
import sys
import webbrowser
import requests
import cv2
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
from requests import get
import pyjokes
import time
import pyautogui
import speedtest
import psutil

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices[1].id)
engine.setProperty("voice", voices[1].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait


# passwaord
def password(pass_inp):
    password = "mini project"
    passs = str(password)
    if passs == str(pass_inp):
        features()
    else:
        speak("who are you?")


# audio to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising.....")
        query = r.recognize_google(audio, language="en-in")
        # f=open("test.txt","a")
        # f.write("\n")
        # f.write(query)
        # f.close()
        f = open("test.txt", "a")
        f.write("------------------------------")
        date = str(datetime.datetime.now().date())
        time = str(datetime.datetime.now().time())

        date = "DATE:->" + date
        time = "TIME:->" + time
        query1 = "MESSAGE:->" + query
        f.write("\n")
        f.write(date)
        f.write("\n")
        f.write(time)
        f.write("\n")
        f.write(query1)
        f.write("\n")

        f.close()
        print(f"user said:{query}")

    except Exception as e:
        speak("say that again please......")
        return "none"
    return query


# to wish


def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour >= 0 and hour < 12:
        speak(f"Good morning,its {tt}  ")
    elif hour >= 12 and hour < 16:
        speak(f"Good afternoon,its {tt}")
    else:
        speak(f"Good evening,its {tt}")
    speak("I am pikaachu , please tell me how can I help you")


def news():
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=0fbc80e9d6a641b58e90aebdf5c0ac6f"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth"]

    # speak("enter no of news you want to listen:")

    # +day= input("enter no of news you want to listen:")

    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's{day[i]} news is :{head[i]}")


def features():
    wish()

    while True:
        # if 1:
        query = takecommand().lower()

        # logic building for tasks

        # (to open and close notepad)

        if "open notepad" in query:
            speak("okay, notepad is here")
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\notepad.lnk"
            os.startfile(npath)

        elif "close notepad" in query:
            speak("okay ,closing notepad")
            os.system("taskkill /f /im notepad.exe")

        # (to open and close vs code)
        elif "open vs code" in query:
            speak("okay, vs code is here")
            cpath = (
                "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            )
            os.startfile(cpath)

        elif "close vs code" in query:
            speak("okay  ,closing vs code")
            os.system("taskkill /f /im code.exe")

        # (to open and close cmd)
        elif "open command prompt" in query:
            speak("okay, cmd is here")
            os.system("start cmd")
        elif "close command prompt" in query:
            speak("okay ,closing command prompt")
            os.system("taskkill /f /im cmd.exe")

        # (to play music)
        elif "play music" in query:
            music_dir = "C:\\Users\\user\\Desktop\\music"
            songs = os.listdir(music_dir)
            # os.startfile(os.path.join(music_dir,songs[0] ))
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        # (top 10 news headlines)
        elif "news" in query:
            speak("please wait,i'm fetching the latest news")
            news()

        # (to ip address from any url)
        elif "ip address" in query:
            speak("enter the url")
            url = input("enter the url:")
            ip = get(url).text
            speak(f"your ip address is{ip}")

        # used for searching  (according to wikipedia)
        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            requests = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(requests)
            # print(requests)

        # (to open youtube and search anything on youtube)
        elif "open youtube" in query:
            speak("okay, what  should  I play on youtube ")
            ac = takecommand().lower()
            pywhatkit.playonyt(ac)

        # (to tell a joke )
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        # (to open facebook)
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        # (to open twitter)
        elif "open twitter" in query:
            webbrowser.open("www.twitter.com")

        # (to open instagram)
        elif "open instagram" in query:
            webbrowser.open(" www.instagram.com")

        # (to search on google)
        elif "open google" in query:
            speak(" what  should  I search on google ")
            cm = takecommand().lower()
            speak("ok,searching.....")
            pywhatkit.search(f"{cm}")

        # (to send whatsapp msg)
        elif "send message" in query:
            speak("what message you want to send")
            message = takecommand().lower()
            time.sleep(3)
            hour = int(datetime.datetime.now().hour)
            min = int(datetime.datetime.now().minute)
            speak("phone number:")
            contact = takecommand().lower()
            contact = "+91" + str(contact)
            pywhatkit.sendwhatmsg_instantly(f"{contact}", message)

        elif "internet speed" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(
                f"we have{dl} bit per second downloading speed and {up} bit per second uploading speed"
            )

        # (to take screenshot)
        elif "take screenshot" in query:
            speak("please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am done, the screenshot is saved in main folder")

        elif "how much battery we have" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"our system have{percentage} percent battery")
            if percentage >= 75:
                speak("we have enough power to continue our work")
            elif percentage >= 40 and percentage <= 30:
                speak(
                    "we should connect our system to charging point to charge our battery"
                )
            elif percentage <= 15 and percentage <= 30:
                speak("we don't have enough power to work, please connect to charging.")
            elif percentage <= 15:
                speak(
                    " our system have very low power, please connect to charging the system will shutdown very soon"
                )

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            img_counter = 0
            while True:
                ret, img = cap.read()
                if not ret:
                    speak("failed")
                    break
                cv2.imshow("test", img)
                # cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k % 256 == 27:
                    speak("escape hit,closing the app")

                    break

                elif k % 256 == 32:
                    img_name = "open cv_img_{}.png".format(img_counter)
                    cv2.imwrite(img_name, img)
                    speak("image taken")
                    img_counter += 1
            cap.release()
            cv2.destroyAllWindows()

        elif "bye pikachu" in query:
            speak("take care")
            speak("bye")
            sys.exit()

        elif "how are you" in query:
            speak("i am fine, what about you")

        elif "also good" in query:
            speak("that's great to hear from you")
        elif "thank you" in query:
            speak("it's my pleasure")


if __name__ == "main":
    while True:
        wakeup = takecommand().lower()

        if "hello pikachu" in wakeup:
            speak("its ready to run")

            speak("it requires password")
            passs = takecommand().lower()
            password(passs)
