import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greet the user based on the current time."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant Sonet. How can I help you today?")

def listen():
    """Listen to user input via microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that. Please say it again.")
        except sr.RequestError:
            speak("There was an issue connecting to the speech recognition service.")
        except Exception as e:
            print(f"Error: {e}")
    return ""

def execute_command(command):
    """Perform tasks based on user input."""
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}.")
    
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {current_date}.")
    
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    
    elif "play music" in command:
        music_dir = "C:\\Users\\YourUsername\\Music"  # Update with your music folder path
        songs = os.listdir(music_dir)
        if songs:
            song = random.choice(songs)
            os.startfile(os.path.join(music_dir, song))
            speak("Playing music.")
        else:
            speak("No music files found in your directory.")
    
    elif "quit" in command or "exit" in command:
        speak("Goodbye! Have a great day!")
        exit()
    
    else:
        speak("Sorry, I can't perform that task right now.")

# Main program
if __name__ == "__main__":
    greet_user()
    while True:
        user_command = listen()
        if user_command:
            execute_command(user_command)
