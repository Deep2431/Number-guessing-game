import random
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
engine.setProperty('volume',1.0)
engine.setProperty('rate',150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

r = sr.Recognizer()

def speak(text):
        engine.say(text)
        engine.runAndWait()
    
def microInput():
        with sr.Microphone() as source:
            print('listening..')
            audio = r.listen(source)
            query = ''
            try:
                query = r.recognize_google(audio)
                print(query)
            except sr.UnknownValueError:
                speak('I did not get that..')
            except sr.RequestError:
                speak('network issues..')
                return "None"
            return query

def numGuess():
    cInp = random.randint(1,100)
    count = 0
    attempts = 5
    speak('You have only 5 attempts, so carefully choose a number')

    while count < attempts:
        print('Choose a number..')
        command = microInput().lower()
        guess = int(command)
        if guess > cInp:
            print('Choose a lower number..')
            speak('Choose a lower number..')
        elif guess < cInp:
            print('Choose a higher number..')
            speak('Choose a higher number..')
        else:
            print("You win!")
            speak("You win!")
            break
        count += 1
        print(f"you have {attempts-count} guesses left")

    if count >= attempts:
        print('Game over!')

numGuess()



    
