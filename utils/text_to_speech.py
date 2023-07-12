import pyttsx3 as tts

engine = tts.init()
engine.setProperty('rate', 125)
engine.setProperty('voice', 'english-us')


def speak(text):
    engine.say(text)
    engine.runAndWait()
