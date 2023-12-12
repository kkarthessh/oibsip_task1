import speech_recognition as sr
import pyttsx3
from datetime import datetime,timedelta
import calendar
import webbrowser
import pyaudio
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def greet():
    speak("Hello!! Mr.Kartheesh! How can I help you today?")
def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"User said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Can you repeat?")
        return ""
    except sr.RequestError as e:
        print(f"Error connecting to Google API: {e}")
        return ""
def execute_command(command):
    if "hello" in command:
        speak("Hello Mr kartheesh !! How can I help you today?")
    elif "time" in command:
        current_time = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "today" in command:
        today = datetime.today()
        speak(f"Today's date is {today}")
    elif "yesterday" in command:
        yesterday = datetime.today() - timedelta(days=1)
        speak(f"Yesterday date is {yesterday}")
    elif "tomorrow" in command:
        tomorrow = datetime.today() + timedelta(days=1)
        speak(f"Tomorrow's date is {tomorrow}")
    elif "search" in command:
        search_query = command.replace("search", "").strip()
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
        speak(f"Here are the search results for {search_query}.")
    elif "exit" in command or "bye" in command:
        speak("Goodbye! Have a good day we will meet you soon.")
        exit()
    else:
        speak("I'm sorry, I don't understand that command.")
if __name__ == "__main__":
    greet()
    while True:
        command = get_command()
        if command:
            execute_command(command)