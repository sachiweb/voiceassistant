import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import pyjokes
import requests
from bs4 import BeautifulSoup


listener= sr.Recognizer()
engine= pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)


# def scraping(req):

#     URL='https://www.google.com/search?q=' + req
#     page=requests.get(URL)
#     soup=BeautifulSoup(page.content, 'html.parser')
#     links=soup.findAll("a")
    # all_link=[]
    # for link in links:
    #     link_href=link.get('href')
    #     if "url?q=" in link_href and not "webcache" in link_href:
    #         all_link.append((link.get('href').split("?q=")[1].split("&sa=u")[0]))
    # flag=False
    # for link in all_link:
    #     if 'http://en.wikipedia.org/wiki' in links:
    #         wiki=link
    #         flag=True
    # return soup


def talk(text):
    engine.say(text)
    engine.runAndWait()
 

def max_command():
    try:
        with sr.Microphone() as source:
            print("listening........")
            talk("hay its max")
            voice= listener.listen(source)
            command= listener.recognize_google(voice)
            command= command.lower()
            if "max" in command:
                command=command.replace("max","")
                print(command)
    except:
        pass
    return command

def run_max():
    command=max_command()
    print(command)
    if "play" in command:
        song=command.replace("play","")
        talk("playing"+song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time=datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("current time is"+time)
    elif "who is" in command:
        persion=command.replace("who is","")
        info=wikipedia.summary(persion,2)
        print(info)
        talk(info)
    elif "open" in command:
        x=command.replace("open","")
        webbrowser.open(x)
        talk("opening")
    elif "open github" in command:
        webbrowser.open("github.com")
        talk("opening")
    elif "open spotify" in command:
        webbrowser.open("spotify.com")
        talk("opening")
    elif "open google search" in command:
        webbrowser.open("google search.com")
        talk("opening")
    elif "your name" in command:
        name="i am max"
        print(name)
        talk(name)
    elif "are you" in command:
        x="i dont really know"
        talk(x)
    elif "joke" in command:
        x= pyjokes.get_joke(language="en", category="all")
        print(x)
        talk(x)
        
    else:
        #print(scraping(command))
        webbrowser.open(command+".com")
    
    # run_max()

run_max()
