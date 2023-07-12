from utils import text_to_speech as tts
from newsapi import NewsApiClient as na
from utils import config

newsapi = na(api_key=config.NEWS_API_KEY)


def get_news(query):
    if query:
        headlines = newsapi.get_top_headlines(q=query, language='en', country='us', page_size=5, page=1)
    else:
        headlines = newsapi.get_top_headlines(language='en', country='us', page_size=5, page=1)

    print('Top headlines')
    print(f"Total results: {headlines['totalResults']}")
    tts.speak('Top headlines')

    for article in headlines['articles']:
        print(article['title'])
        tts.speak(article['title'])

        print('Would you like to know more?')
        tts.speak('Would you like to know more?')

        print('1. Yes')
        tts.speak('1. Yes')

        print('2. No')
        tts.speak('2. No')

        choice = input('Enter your choice: ')
        print()
        if choice == '1':
            print(article['description'])
            tts.speak(article['description'])
        elif choice == '2':
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

    choice = input('Enter your choice: ')
    if choice == '1':
        get_news(None)
    elif choice == '2':
        query = input('Enter your query: ')
        get_news(query)
    elif choice == '3':
        print('Exiting news assistant')
        tts.speak('Exiting news assistant')
