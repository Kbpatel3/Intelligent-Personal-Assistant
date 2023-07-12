import speech_recognition as sr
import pyttsx3 as tts
from assistants import weather, time, joke, news, wikipedia, web_search
from utils import nlp


def process_command(command):
    intent = nlp.extract_intent(command)

    if intent == 'greeting':
        print('Hello, how can I help you?')
        tts.speak('Hello, how can I help you?')
    elif intent == 'goodbye':
        print('Goodbye!')
        tts.speak('Goodbye!')
        exit()
    elif intent == 'weather':
        weather.handle_command()
    elif intent == 'time':
        time.handle_command()
    elif intent == 'joke':
        joke.handle_command()
    elif intent == 'news':
        news.handle_command()
    elif intent == 'wikipedia':
        wikipedia.handle_command()
    elif intent == 'google':
        web_search.handle_command()
    else:
        print('Sorry, I did not get that')
        tts.speak('Sorry, I did not get that')


def main():
    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as mic:
                r.adjust_for_ambient_noise(mic, duration=1.0)
                print('Listening...')
                audio = r.listen(mic, timeout=5, phrase_time_limit=5)
                print("Processing...")
                text = r.recognize_google(audio)
                text = text.lower()
                print(f'You said: {text}')
                process_command(text)
        except sr.UnknownValueError:
            print('Sorry, I did not get that')
            r = sr.Recognizer()
            continue
        except sr.RequestError as e:
            print(f'Sorry, my speech service is down {e}')
            r = sr.Recognizer()
            continue
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected")
            r = sr.Recognizer()
            continue


if __name__ == '__main__':
    main()
