import pyttsx3 as tts
from assistants import weather, time, joke, news, wikipedia, web_search
from utils import nlp
from utils import speech_recognition as srutils
import speech_recognition as sr


def process_command(command):
    intent = nlp.extract_intent(command)

    if intent == 'greeting':
        print('Hello, how can I help you?')
        tts.speak('Hello, how can I help you?')
        process_command(srutils.recognize())
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
        print('Intent not recognized')
        tts.speak('Intent not recognized')


def main():
    while True:
        try:
            await_text = srutils.recognize()
            if nlp.extract_intent(await_text) == 'assistant':
                print("Assistant activated")
                tts.speak("Assistant activated")
                speech_text = srutils.recognize()
                process_command(speech_text)
        except sr.UnknownValueError:
            continue
        except sr.RequestError as e:
            print(f'Sorry, my speech service is down {e}')
            tts.speak('Sorry, my speech service is down')
            continue
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected")
            continue


if __name__ == '__main__':
    main()
