import nltk
nltk.download('punkt')
nltk.download('stopwords')


def extract_intent(command):
    # Tokenize the command
    tokens = nltk.word_tokenize(command)

    # Remove stop words
    stop_words = nltk.corpus.stopwords.words('english')
    tokens = [token for token in tokens if token not in stop_words]

    intents = {
        'greeting': ['hello', 'hi', 'hey', 'good morning', 'good evening', 'good afternoon'],
        'goodbye': ['bye', 'goodbye', 'see you later', 'take care', 'see you soon'],
        'weather': ['weather', 'temperature', 'climate', 'rain', 'sun', 'cloud', 'hot', 'cold'],
        'time': ['time', 'clock', 'hour', 'minute', 'second', 'day', 'month', 'year'],
        'joke': ['joke', 'laugh', 'funny', 'hilarious', 'humor', 'comedy'],
        'news': ['news', 'headline', 'current', 'affairs', 'newspaper', 'article'],
        'wikipedia': ['wikipedia', 'wiki', 'information', 'search'],
        'google': ['google', 'search', 'find', 'look up']
    }

    # Check if the command contains any of the intents
    for intent, keywords in intents.items():
        if any(keyword in tokens for keyword in keywords):
            return intent
