import nltk
import spacy
import arrow

nltk.download('punkt')
nltk.download('stopwords')


def extract_intent(command):
    # Tokenize the command
    tokens = nltk.word_tokenize(command)

    # Remove stop words
    stop_words = nltk.corpus.stopwords.words('english')
    tokens = [token for token in tokens if token not in stop_words]

    # SpaCy for NER (Named Entity Recognition)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(command)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    intents = {
        'assistant': ['assistant'],
        'greeting': ['hello', 'hi', 'hey', 'good morning', 'good evening', 'good afternoon'],
        'goodbye': ['bye', 'goodbye', 'see you later', 'take care', 'see you soon'],
        'weather': ['weather', 'temperature', 'climate', 'rain', 'sun', 'cloud', 'hot', 'cold'],
        'time': ['time', 'clock', 'hour', 'minute', 'second', 'day', 'month', 'year'],
        'joke': ['joke', 'laugh', 'funny', 'hilarious', 'humor', 'comedy'],
        'news': ['news', 'headline', 'current', 'affairs', 'newspaper', 'article'],
        'wikipedia': ['wikipedia', 'wiki', 'information', 'search'],
        'google': ['google', 'search', 'find', 'look up'],
        'yes': ['yes', 'yeah', 'sure', 'ok', 'okay', 'fine', 'yup', 'yep'],
        'no': ['no', 'nope', 'nah', 'not', 'negative'],
        'exit': ['exit', 'quit', 'stop', 'terminate', 'end'],
        'one': ['1', 'one'],
        'two': ['2', 'two'],
        'three': ['3', 'three'],
        'top headlines': ['top headlines', 'headlines', 'top'],
        'news search': ['search', 'query', 'find', 'look up']
    }

    # Check if the command contains any of the intents
    for intent, keywords in intents.items():
        if any(keyword in tokens for keyword in keywords):
            return intent

    # Dictionary for time parameters
    parameters = {}

    # Check if the command contains any of the entities
    for entity, label in entities:
        if label == 'GPE' and 'time' in tokens:
            parameters['location'] = entity
            return 'time in location', parameters
        elif label == 'TIME':
            return 'current time', parameters

    # Date/Time parsing
    if 'date' in tokens:
        return 'current date'
    elif 'day' in tokens and 'week' in tokens:
        return 'current day of the week'
    elif 'time zone' in command or 'time in' in command:
        return 'time zone conversion'
    elif 'event' in tokens and ('time' in tokens or 'start' in tokens or 'end' in tokens):
        return 'time of event'
    elif 'duration' in tokens or 'long' in tokens:
        return 'time duration'
    elif 'calculate' in tokens and 'time' in tokens:
        return 'time calculation'
    elif 'past' in tokens or 'future' in tokens:
        return 'time in the past/future'
    elif any(arrow.get(token, ['h:mm A', 'H:mm']).format('') == token for token in tokens):
        return 'time format'
