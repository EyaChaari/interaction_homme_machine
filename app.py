import speech_recognition as sr  # recognise speech
import playsound  # to play an audio files
from gtts import gTTS  # google text to speech
import random
from time import ctime  # get time details
import webbrowser  # open browser
import ssl
import certifi
import time
import os  # to remove created audio files
from PIL import Image
import subprocess
import pyautogui  # screenshot
import pyttsx3
import bs4 as bs
import urllib.request


class person:
    name = ''

    def setName(self, name):
        self.name = name


class asis:
    name = ''

    def setName(self, name):
        self.name = name


engine = pyttsx3.init()
voices = engine.getProperty('voices')


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()  # initialise a recogniser


# listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source:  # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError:  # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down')  # error: recognizer is not connected
        print(">>", voice_data.lower())  # print what user said
        return voice_data.lower()


def engine_speak(audio_string):
    audio_string = str(audio_string)
    print(asis_obj.name + ":", audio_string)  # Afficher ce qui est dit
    engine.say(audio_string)  # Utilisation de pyttsx3
    engine.runAndWait()


def respond(voice_data):
    # 1: greeting
    if there_exists(['hey', 'hi', 'hello']):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name,
                     "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name,
                     "hello" + person_obj.name]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        engine_speak(greet)

    # 2: name
    if there_exists(["what is your name", "what's your name", "tell me your name"]):
        if person_obj.name:
            engine_speak("whats with my name ")
        else:
            engine_speak("i dont know my name . what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name)  # remember name in person object

    if there_exists(["your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name)  # remember name in asis object

    # 3: greeting
    if there_exists(["how are you", "how are you doing"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)

    # 4: time
    if there_exists(["what's the time", "tell me the time", "what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        engine_speak(time)

    # 5: search google

    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")

    # 7: get stock price

    if there_exists(["price of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")

    # search for music
    if there_exists(["play music"]):
        search_term = voice_data.split("for")[-1]
        url = "https://open.spotify.com/search/" + search_term
        webbrowser.get().open(url)
        engine_speak("You are listening to" + search_term + "enjoy sir")
    # search for amazon.com
    if there_exists(["amazon.com"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.amazon.in" + search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for" + search_term + "on amazon.com")

    # make a note
    if there_exists(["make a note"]):
        search_term = voice_data.split("for")[-1]
        url = "https://keep.google.com/#home"
        webbrowser.get().open(url)
        engine_speak("Here you can make notes")

    # open instagram

    if there_exists(["open instagram", "want to have some fun time"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("opening instagram")

    # open twitter

    if there_exists(["open twitter"]):
        search_term = voice_data.split("for")[-1]
        url = "https://twitter.com/"
        webbrowser.get().open(url)
        engine_speak("opening twitter")

    # weather

    if there_exists(["weather", "tell me the weather report", "whats the condition outside"]):
        search_term = voice_data.split("for")[-1]
        url = "m"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")

    # open gmail
    if there_exists(["open my mail", "gmail", "check my email"]):
        search_term = voice_data.split("for")[-1]
        url = "https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        engine_speak("here you can check your gmail")

    # 10 stone paper scisorrs

    if there_exists(["game"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves = ["rock", "paper", "scissor"]

        cmove = random.choice(moves)
        pmove = voice_data

        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        # engine_speak("hi")
        if pmove == cmove:
            engine_speak("the match is draw")
        elif pmove == "rock" and cmove == "scissor":
            engine_speak("Player wins")
        elif pmove == "rock" and cmove == "paper":
            engine_speak("Computer wins")
        elif pmove == "paper" and cmove == "rock":
            engine_speak("Player wins")
        elif pmove == "paper" and cmove == "scissor":
            engine_speak("Computer wins")
        elif pmove == "scissor" and cmove == "paper":
            engine_speak("Player wins")
        elif pmove == "scissor" and cmove == "rock":
            engine_speak("Computer wins")

    # 11 toss a coin

    if there_exists(["toss", "flip", "coin"]):
        moves = ["head", "tails"]
        cmove = random.choice(moves)
        engine_speak("The computer chose " + cmove)

    # 12 calc
    if there_exists(["plus", "minus", "multiply", "divide", "power", "+", "-", "*", "/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")

    # 13 screenshot

    if there_exists(["capture", "my screen", "screenshot"]):
        folder_path = r'C:\captures'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'C:\captures\screenshot.png')



    if there_exists(["definition of"]):
        definition = record_audio("what do you need the definition of")
        url = urllib.request.urlopen('https://en.wikipedia.org/wiki/' + definition)
        soup = bs.BeautifulSoup(url, 'lxml')
        definitions = []
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                engine_speak('im sorry i could not find that definition, please try a web search')
            elif definitions[1]:
                engine_speak('here is what i found ' + definitions[1])
            else:
                engine_speak('Here is what i found ' + definitions[2])
        else:
            engine_speak("im sorry i could not find the definition for " + definition)

    if there_exists(["exit", "quit", "goodbye"]):
        engine_speak("Good bye,have a nice day!")
        exit()


time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'Alexa'
engine = pyttsx3.init()

while (1):
    voice_data = record_audio("Recording")  # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data)#  respond
