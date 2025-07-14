import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import os
import time

# Initialize voice engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your assistant. How can I help you today?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("🧠 Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"👉 You said: {query}")
    except Exception:
        print("❌ Sorry, I didn't get that.")
        return "None"
    return query.lower()

def main():
    wish_user()
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'open chrome' in query:
            speak("Opening Google Chrome")
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab("https://www.google.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'play' in query:
            song = query.replace('play', '')
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        elif 'open notepad' in query:
            speak("Opening Notepad")
            os.system("notepad.exe")

        elif 'joke' in query or 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'send whatsapp message' in query:
            speak("Tell me the phone number with country code")
            number = take_command().replace(" ", "")
            speak("What message should I send?")
            message = take_command()
            speak("Sending message...")
            try:
                pywhatkit.sendwhatmsg_instantly(f"+{number}", message)
                speak("Message sent successfully!")
            except Exception as e:
                speak("Sorry, I couldn't send the message.")
                print(e)

        elif 'stop' in query or 'bye' in query:
            speak("Goodbye! See you later.")
            break

if __name__ == "__main__":
    main()
