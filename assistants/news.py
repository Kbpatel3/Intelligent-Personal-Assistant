from utils import config
from newsapi import NewsApiClient as na
import speech_recognition as sr

newsapi = na(api_key=config.NEWS_API_KEY)


def handle_command(tts, recognizer):
    headlines = newsapi.get_top_headlines(language='en', country='us', page_size=5, page=1)

    print('The top headlines are: ')
    tts.speak('The top headlines are: ')
    for article in headlines['articles']:
        print(article['title'])
        tts.speak(article['title'])

        print('Would you like to know more?')
        tts.speak('Would you like to know more?')

        print('Listening...')
        audio = recognizer.listen(sr.Microphone())
        print("Processing...")
        text = recognizer.recognize_google(audio)
        text = text.lower()

        if text == 'yes':
            print(article['description'])
            tts.speak(article['description'])
            tts.speak('Moving on to the next article')
        elif text == 'no':
            continue
