# pip install pyttsx3 for speak out ,or text
# pip install speech Recognition for the robot to listen to our voice speech
# pip install pywhatkit for advance control on browser
# pip install wikipedia for to get wikipedia data
# pip install pyjokes to get funny jokes.

# import librarries
from time import strftime
import speech_recognition as sr

# r = sr.Recognizer()

import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now()('%H:%M')
        talk('Current time is' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say the command again')

while True:
    run_alexa()