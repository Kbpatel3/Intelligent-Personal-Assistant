import speech_recognition as sr
import pyttsx3 as tts
from neuralintents import GenericAssistant
from playsound import playsound
import sys
from assistants import news


class Assistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty('rate', 150)

        self.assistant = GenericAssistant('intents.json', intent_methods={
            'news': self.news,
        })
        self.assistant.train_model()

    def news(self):
        self.speaker.say('Getting news')
        self.speaker.runAndWait()
        news.handle_command(self.speaker, self.recognizer)

    def run_assistant(self):
        while True:
            try:
                with sr.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    print('Listening...')
                    audio = self.recognizer.listen(mic)
                    print("Processing...")
                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()
                    print(f'You said: {text}')

                    if "hey assistant" in text:
                        playsound('utils/sounds/assistant_activated.mp3', block=False)
                        print('Listening...')
                        audio = self.recognizer.listen(mic)
                        print("Processing...")
                        text = self.recognizer.recognize_google(audio)
                        text = text.lower()
                        if text == 'exit':
                            print('Exiting assistant')
                            self.speaker.say('Exiting assistant')
                            self.speaker.runAndWait()
                            self.speaker.stop()
                            sys.exit()
                        else:
                            if text is not None:
                                response = self.assistant.request(text)
                                if response is not None:
                                    self.speaker.say(response)
                                    self.speaker.runAndWait()
            except:
                continue


if __name__ == '__main__':
    Assistant()
