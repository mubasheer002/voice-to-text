import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyaudio

listener =sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
def takecommand():
    try:
        with sr.Microphone() as source:
            print("listening......")
            voice =listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'alexa'in command:
                command = command.replace('alexa','')



    except:
        pass
    return command

def runalexa():
    command = takecommand()
    print(command)
    if 'play'in command:
        song = command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'youtube'in command:
        song = command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M ')
        talk('current time is '+time)
    elif 'who is'in command:
        wiki=command.replace('who is','')
        info = wikipedia.summary(wiki)
        #print(info)
        talk(info)
    elif 'my name'in command:
        talk('your name is mubasheer')
runalexa()