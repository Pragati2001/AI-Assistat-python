import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import time
def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening")
        audio=r.listen(source,phrase_time_limit=10)
    data=""
    try:
        data=r.recognize_google(audio,language='en-US')
        print("You said: "+data)
    except sr.UnknownValueError:
        print("I cannot hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data
def respond(String):
    print(String)
    tts=gTTS(text=String,lang="en")
    tts.save("Speech.mp3")
    playsound.playsound("Speech.mp3")
    os.remove("Speech.mp3")
def voice_assistant(data):
    if "Who are you" in data:
        listening=True
        respond("I am your assistant")
    if "how are you" in data:
        listening=True
        respond("I am Well")
    try:
        return listening
    except UnboundLocalError:
        print("TimedOut-->Re-Launch")
time.sleep(2)
respond("Hello what can i do fr you")
listening=True
while listening==True:
    data=listen()
    listening=voice_assistant(data)


