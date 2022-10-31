# from _typeshed import WriteableBuffer


from pyaudio import paNoDevice
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyautogui
import pywhatkit as pwk
import pyjokes as pj
import requests
from tkinter import *
import os
import wolframalpha
import ctypes
import random


min=1
max=6
root = Tk()
path = os.getcwd()
var = StringVar()
var1 = StringVar()
frameCnt = 32

frames = [PhotoImage(file=path+'/jarvis-iron-man.gif',format= 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(background='black')
    label.configure(image=frame)
    root.after(100, update, ind)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        var.set("Good Morning!")
        root.update
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        var.set("Good Afternoon!")
        root.update()
        speak("Good Afternoon!")

    else:
        var.set("Good Evening!")
        root.update()
        speak("Good Evening!")

    var.set("I am Jarvis Sir. How may I help you?")
    root.update()
    speak("I am Jarvis Sir. How may I help you?")


def takeCommand():
    # It takes microphone in put from the  user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        root.update()
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    
    

    try:
        var.set("Recognizing...")
        root.update
        print("Recognising...")
        # r.adjust_for_ambient_noise(source,duration = 3)
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        var1.set(query)
        root.update

    except Exception as e:
        var.set("Say that again please...")
        root.update()
        print("Say that again please...")
        return "None"

    return query


def get_weather(city):
    result = requests.get(url.format(city, '99c9db04fb83ce087fb75dedc820a6ae'))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_farenheit = (temp_celsius) * 9/5 + 32
        weather = json['weather'][0]['main']
        a = str(temp_celsius)
        temp_celsius = a[0:4]
        final = (city, country, temp_celsius, temp_farenheit, weather)
        print(final)
        var.set(
            f"Today it is {weather} in {city} and the temprature is {temp_celsius} degree celsius ")
        root.update()
        speak(
            f"Today it is {weather} in {city} and the temprature is {temp_celsius} degree celsius ")
        print(
            f"Today it is {weather} in {city} and the temprature is {temp_celsius} degree celsius ")


def Commands():
    file = path+"/command.txt"
    file1 = open(file, "a")

def runJarvis():
    wishMe()
    while True:
        # btn2['state'] = 'disabled'
        # btn3['state'] = 'disabled'
        btn1.configure(bg='orange')

        query = takeCommand().lower()
        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            var.set("Searching Wikipedia...")
            root.update()
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            var.set(results)
            root.update()
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            var.set(f"opening {location} on google maps wait a second")
            root.update()
            speak(f"opening {location} on google maps wait a second")
            webbrowser.open("https://www.google.co.in/maps/place/ " + location)

        elif 'open youtube' in query:
            var.set("Opening Youtube...")
            root.update
            speak("Opening Youtube ..")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            var.set("Opening Google...")
            root.update()
            speak("Opening Google...")
            webbrowser.open("google.com")

        elif 'open code' in query:
            var.set("Open Code")
            root.update()
            speak("Opening VS Code")
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open microsoft teams' in query:
            var.set("Open Microsoft Teams")
            root.update()
            speak("Opening MS Teams")
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
            os.startfile(codePath)
        
        elif 'open stack overflow' in query:
            var.set("Opening stack overflow...")
            root.update
            speak("Opening Stackoverflow... Happy Coding")
            webbrowser.open("stackoverflow.com")

        elif 'open study material' in query:
            var.set("open study material")
            root.update
            speak("Opening study material... Have a Good Study session")
            webbrowser.open("studease.vidyalankar.org")

        elif 'open payment screen' in query:
            var.set("open payment screen")
            root.update
            speak("Opening payment screen")
            webbrowser.open("payumoney.com/customer/users/paymentOptions/#/7BE48615C376225262864096A743A78F/VITLINK/211643")

        elif ' time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set(f"Sir, the time is {strTime}")
            root.update()
            speak(f"The time is {strTime}")

        elif 'screenshot' in query:
            im1 = pyautogui.screenshot()
            im1.save('my_screenshot.png')
            # im2 = pyautogui.screenshot('my_screenshot2.png')
            var.set("Screenshot taken")
            root.update()
            speak("Screenshot has been taken and saved sucessfully..")


        elif 'play' in query:
            song = query.replace('play', '')
            var.set("playing"+song)
            root.update()
            speak("playing"+song)
            print("  playing"+song)
            pwk.playonyt(song)      

        elif 'weather' in query:

            if "tell me about today's weather in" in query:
                query = query.replace("tell me about today's weather in ", "")
                city = query

            elif "what is today's weather" in query:
                speak("Which city do you want to know the weather of")
                city = takeCommand()
            get_weather(city)

        elif 'joke' in query:
            joke = pj.get_joke()
            var.set(joke)
            var1.set(joke)
            root.update
            print(joke)
            speak(joke)
            

        elif 'hello' in query:
            var.set('Hello Sir')
            root.update()
            speak("Hello Sir")

        elif 'who created you' in query:
            var.set("My creators are Priyanshu Tejas Madiha and Dipesh")
            root.update()
            speak("My creators are Priyanshu Tejas Madiha and Dipesh")

        elif 'go to sleep' in query:
            var.set("Thanks for giving me your time")
            root.update()
            speak("Thanks for giving me your time")
            return None

        elif "what can you do" in query:
            var.set(
                "I can perform various functions like opening apps,opening websites ,play songs on youtube ,tell you a joke etc")
            root.update()
            speak(
                "I can perform various functions like opening apps,opening websites,play songs on youtube,tell you a joke etc")

        elif "who are you" in query:
            var.set("I am Jarvis your voice assistant")
            root.update()
            speak("I am Jarvis your voice assistant")

        elif "good" in query:
            var.set("great to hear that")
            root.update()
            speak("great to hear that")
        
        elif "calculate" in query:
             
            app_id = "3TUW68-KJUQY8T2WH"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            var.set("The answer is " + answer)
            root.update()
            speak("The answer is " + answer)
        
        elif 'lock desktop' in query:
            var.set("Locking the Device")
            root.update()
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        
        elif 'roll a dice' in query:
                speak("Here you go")
                var.set("Here you go")
                root.update()
                print("Rolling the dice...")               
                speak("Rolling the dice...")
                var.set("Rolling the dice...")
                root.update()               
                dice = random.randint(min, max)              
                print(f'{"The Dice Number Rolled is "}{dice}')
                var.set(f'{"The Dice Number Rolled is "}{dice}')
                root.update()
                speak(f'{"The Dice Number Rolled is "}{dice}')


def Commands():
    command_window = Toplevel(root, bg="black")
    command_window.title("JARVIS commands")
    command_window.geometry('600x180')
    commands = Label(command_window, text="1) Send a message on whatsapp - to send a whatsapp msg.\n2) Open google/youtube/wikipedia/stackoverflow. \n3) Tell me about today's weather - give u weather report of a city. \n4) Where is [cityname]-opens google maps and shows location. \n5) What is the time - tells the current time.\n6) Tell me a joke.\n7) Search something on wikipedia. \n8) Send a mail to someone.\n9) Play [song-name]", font=(
        "Courier", 10), bg="black", foreground="#F2AA4C", justify=LEFT)
    commands.grid()


root.title("JARVIS")
menubar = Menu(root, background="#101820", fg='#F2AA4C')
menubar.add_command(label="Commands", command=Commands)
root.config(menu=menubar)
label2 = Label(root, textvariable=var1, bg='#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(root, textvariable=var, bg='#ADD8E6', wraplength=1200)
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

label = Label(root, height=500, width=800)
label.pack()
root.after(0, update, 0)

btn1 = Button(text='START', command=runJarvis, width=80, bg='#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()

#btn2 = Button(text="WISH ME",command= wishMe,width= 20,bg='#5C85FB')
#btn2.config(font=("Courier",12))
#btn2.pack()

btn3 = Button(text='EXIT', command=root.destroy, width=80, bg='#5C85FB')
btn3.config(font=("Courier", 12))
btn3.pack()
root.configure(background='black')
root.mainloop()