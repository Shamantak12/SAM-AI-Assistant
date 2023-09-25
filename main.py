import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio

print("Initializing SAM")
MASTER = "shamant"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():

    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("Good morning"+ MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon"+MASTER)
    else:
        speak("Good Evening"+MASTER) 
    #speak(" how are you doing today")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        query = None
    return query
speak("Initializing SAM...")
wishMe()
query = takeCommand()
if 'wikipedia' in query.lower():
    speak("Searching wikipedia...")
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query,sentences=2)
    print(results)
    speak(results)
elif 'open youtube' in query.lower():
    webbrowser.open("youtube.com")
elif 'open google' in query.lower():
    webbrowser.open("google.com")
elif 'open stackoverflow' in query.lower():
    webbrowser.open("stackoverflow.com")
elif 'play music' in query.lower():
    music_dir = 'D:\\songs'
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir,songs[0]))
elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strTime}")
elif 'open code' in query.lower():
    codePath = "C:\\Users\\shamant\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)
elif 'email to shamant' in query.lower():
    try:
        speak("what should i say?")
        content = takeCommand()
        to = "shamantanayak@gmail.com"
        sendEmail(to,content)
        speak("Email has been sent")
    except Exception as e:
        print(e)
        speak("Sorry my friend shamant anna. I am not able to send this email")
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password ')
    server.sendmail('shamantanayak@gmail.com  ',to,content)
    server.close()
