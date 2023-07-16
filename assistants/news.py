from utils import text_to_speech as tts
from newsapi import NewsApiClient as na
from utils import config
from utils import nlp
from utils import speech_recognition as srutils

newsapi = na(api_key=config.NEWS_API_KEY)


def get_news(query):
    if query:
        headlines = newsapi.get_top_headlines(q=query, language='en', country='us', page_size=5, page=1)
    else:
        headlines = newsapi.get_top_headlines(language='en', country='us', page_size=5, page=1)

    print(f"Total results: {headlines['totalResults']}")
    if headlines['totalResults'] == 0:
        print('No results found')
        tts.speak('No results found')
        return

    print('The top headlines are: ')
    tts.speak('The top headlines are: ')
    for article in headlines['articles']:
        print(article['title'])
        tts.speak(article['title'])

        print('Would you like to know more?')
        tts.speak('Would you like to know more?')

        intent = nlp.extract_intent(srutils.recognize())
        print()
        if intent == 'yes':
            print(article['description'])
            tts.speak(article['description'])
            tts.speak('Moving on to the next article')
        elif intent == 'no':
            continue


def handle_command():
    print('News assistant')
    tts.speak('News assistant')

    print('What would you like to know?')
    tts.speak('What would you like to know?')

    print('1. Top headlines')
    tts.speak('1. Top headlines')

    print('2. Search')
    tts.speak('2. Search')

    print('3. Exit')
    tts.speak('3. Exit')

    intent = nlp.extract_intent(srutils.recognize())

    print(intent)
    if intent == 'one' or intent == 'top headlines':
        get_news(None)
    elif intent == 'two' or intent == 'search' or intent == 'wikipedia' or intent == 'google':
        print("What would you like to know about?")
        tts.speak("What would you like to know about?")

        query = srutils.recognize()

        get_news(query)
    elif intent == 'three' or intent == 'exit':
        print('Exiting news assistant')
        tts.speak('Exiting news assistant')
