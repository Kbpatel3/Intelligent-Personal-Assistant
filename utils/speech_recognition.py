import speech_recognition as sr
from playsound import playsound


def recognize(ping=True):
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic, duration=1.0)
        print('Listening...')
        if ping:
            playsound('utils/sounds/assistant_activated.mp3', block=False)
        audio = r.listen(mic, timeout=5, phrase_time_limit=5)
        print("Processing...")
        text = r.recognize_google(audio)
        text = text.lower()
        print(f'You said: {text}')
        return text
