# Voice assistant using python
# author: raufursimanto03065@gmail.com
# date: 17/8/2020


import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import time
import requests as r

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    """Convert text to audio"""
    engine.say(audio)
    engine.runAndWait()


def commands():
    """show all the commands. Pass them to speak() to convert audio"""

    print("1. To search in wikipedia say, 'search item' wikipedia")
    speak("1. To search in wikipedia, say 'search item' wikipedia")

    print("2. To open google, youtube, facebook,stackoverflow say, open 'search item'")
    speak("2. To open google, youtube, facebook,stackoverflow, say open 'search item'")

    print("3. To play music say, play music")
    speak("3. To play music, say play music")

    print("4. To play video say, play video")
    speak("4. To play video, say play video")

    print("5. To see image say, show an image")
    speak("5. To see image, say show an image")

    print("6. For top news, say, top news")
    speak("6. For top news, say top news")

    print("7. To know current time say, current time")
    speak("7. To know current time, say current time")

    print("8. To stop this application say, quit")
    speak("8. To stop this application, say quit")

    speak("Now, please give your command")


def wishMe():
    """ Wishes based on current time and call commands method"""

    hour = int(datetime.datetime.now().hour)
    time.sleep(0.5)
    if hour >= 0 and hour < 12:
        speak('Good Morning')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak('Sir,I am Zira. Voice feature of this application. This application can perform following commands')
    commands()


def takeCommand():
    """ Take audio as command.
    First recognize audio query using Recognizer() method and print command.
    Can handle errors"""

    r = sr.Recognizer()
    r.energy_threshold = 4000

    with sr.Microphone() as source:
        print('Listening........')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please...")
        return "None"  # None string will be returned

    return query


def play_video(new_path):
    """ find mp4 or mkv file using os module and return the path of this file"""

    for roots, dirs, files in os.walk(new_path):
        for file in files:
            if file.endswith('.MKV') or file.endswith('.mp4'):
                return os.path.join(roots, file)


def showImage(newpath):
    """ find 'jpg' or 'png' file using os module and return the file path"""

    for roots, dirs, files in os.walk(newpath):
        for file in files:
            if file.endswith('png') or file.endswith('jpg'):
                return os.path.join(roots, file)


def playMusic(new_path):
    """ find 'mp3' file using os module and return the file path"""

    for roots, dirs, files in os.walk(new_path):
        for file in files:
            if file.endswith('.mp3') or file.endswith('.wav'):
                return os.path.join(roots, file)


def readNews(info):
    """print the news from given link and convert to audio using speak()"""

    speak("Today's top 10 news are:")
    for i in range(0, 10):
        news = info['articles'][i]['title']
        print(f"{i + 1}: {news} \n")
        speak(f"{i + 1}: {news} \n")

    speak("Thanks for listening")


if __name__ == '__main__':
    wishMe()
    print('\n')

    while True:
        query = takeCommand().lower()  # convert all voice cmd to lowercase

        if 'wikipedia' in query:
            speak('Searching wikipedia.....')
            query = query.replace("wikipedia", "")
            # get 2 lines about given topic
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            try:
                firefox = webbrowser.Mozilla(
                    "C:\\Program Files\\Mozilla Firefox\\firefox.exe")
                firefox.open('http://www.youtube.com')
            except:
                webbrowser.open(youtube.com)

        elif 'open google' in query:
            try:
                firefox = webbrowser.Mozilla(
                    "C:\\Program Files\\Mozilla Firefox\\firefox.exe")
                firefox.open('http://www.google.com')
            except:
                webbrowser.open(google.com)

        elif 'open facebook' in query:
            try:
                firefox = webbrowser.Mozilla(
                    "C:\\Program Files\\Mozilla Firefox\\firefox.exe")
                firefox.open('http://www.facebook.com')
            except:
                webbrowser.open(facebook.com)

        elif 'open stack overflow' in query:
            try:
                firefox = webbrowser.Mozilla(
                    "C:\\Program Files\\Mozilla Firefox\\firefox.exe")
                firefox.open('http://www.stackoverflow.com')
            except:
                webbrowser.open(stackoverflow.com)

        elif 'time' in query:
            # convert current time to minute, hour and sec
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, current time is {strTime}")

        elif 'show image' in query or 'image' in query:
            rootPaths = ['C:\\Users', 'D:\\', 'E:\\',
                         'F:\\', 'G:\\']  # rootpaths of pc

            """all the paths are traversed to find given type of file"""
            for i in range(len(rootPaths)):
                path = rootPaths[random.randint(0, len(rootPaths) - 1)]
                if showImage(path) != None:
                    image_path = showImage(path)
                    break
            os.startfile(image_path)

        elif 'play music' in query or 'music' in query:
            rootPaths = ['C:\\Users', 'D:\\', 'E:\\', 'F:\\', 'G:\\']

            """all the paths are traversed to find given type of file"""
            for i in range(len(rootPaths)):
                path = rootPaths[random.randint(0, len(rootPaths) - 1)]
                if playMusic(path) != None:
                    music_path = playMusic(path)
                    break
            os.startfile(music_path)

        elif 'play video' in query or 'video' in query:
            rootPaths = ['C:\\Users', 'D:\\', 'E:\\', 'F:\\', 'G:\\']

            """all the paths are traversed to find given type of file"""
            for i in range(len(rootPaths)):
                path = rootPaths[random.randint(0, len(rootPaths) - 1)]
                if play_video(path) != None:
                    video_path = play_video(path)
                    break
            os.startfile(video_path)

        elif 'todays top news' in query or 'top news' in query or 'news' in query:
            url = ('http://newsapi.org/v2/top-headlines?'
                   'country=us&'
                   'apiKey=d1040c88648d478cac3f5e6418c2f8e9')
            try:
                response = r.get(url)  # getting news from given url
                info = response.json()  # convert results to json frmat
                readNews(info)

            except Exception as e:
                print(e)

        elif 'quit' in query:
            exit()
