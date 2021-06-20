'''
Author:Neeraj
Date: 19 june 2021
'''

import pyttsx3
from datetime import datetime
import speech_recognition
import wikipedia
import webbrowser
import os
from random import randint
from pywhatkit import playonyt
import pyjokes
import wolframalpha


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("Hi, I'm alexa Speed 1 terahertz, memory 1 zigabyte,  how can i help you")


def takeCommand():
    """Its take microphone input from user and return strings"""
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognzing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said {query}\n")
        except Exception as error:
            print('Your last command couldn\'t be heard ! I can understand commands open google, play songs, open gmail, open website xyz.com and tell me a joke')
            return "None"
        return query


if __name__ == "__main__":
    while True:
        starting = takeCommand().lower()
        if "alexa" in starting:
            wish_me()
            break
while True:
    query = takeCommand().lower()
    if "wikipedia" in query:
        speak("Searching wikipedia...")
        query = query.replace("wikipedia", "")
        print(query)
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak("According to wikipedia")
        speak(results)

    elif "open youtube" in query:
        webbrowser.open("youtube.com")

    elif "open google" in query:
        webbrowser.open("google.com")

    elif "stackoverflow" in query:
        webbrowser.open("stackoverflow.com")

    elif "play music offline" in query:
        music_dir = "D:\\Music"  # path of music directory
        songs = os.listdir(music_dir)
        random_song = randint(0, len(songs)-1)
        os.startfile(os.path.join(music_dir, songs[random_song]))

    elif "play" in query:
        song_name = query.replace("play", "")
        print("playing query")
        playonyt(query)

    elif "time" in query:
        time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")
        print(time)
    elif "open code" in query:
        code_path = r"C:\Users\neera\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        os.startfile(code_path)
    elif "joke" in query:
        speak(pyjokes.get_joke())

    elif "search" in query:
        url = query.replace("search", "")
        webbrowser.open_new_tab(url)

    elif "tell me" in query:
        with open("wolframalpha_api_id.txt", "r") as api_key:
            api_id = api_key.read()
        question = query.replace("tell me", "")
        client = wolframalpha.Client(api_id)
        res = client.query(question)
        answer = next(res.results).text # to make sure wolramalpha gives answer in text and not in graph and all
        print(answer)
        speak(answer)

    elif "quit" in query:
        exit()
