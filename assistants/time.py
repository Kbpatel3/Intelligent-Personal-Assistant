from utils import text_to_speech as tts, nlp, speech_recognition as srutils
import arrow


def get_current_time():
    current_time = arrow.now().format('hh:mm A')
    return f'The current time is {current_time}'


def get_current_date():
    current_date = arrow.now().format('dddd, MMMM D, YYYY')
    return f'The current date is {current_date}'


def get_day_of_week():
    day_of_week = arrow.now().format('dddd')
    return f'Today is {day_of_week}'


def get_time_in_timezone(location):
    try:
        time_in_timezone = arrow.now(location).format('hh:mm A')
        return f'The time in {location} is {time_in_timezone}'
    except arrow.parser.ParserError:
        return f'Location {location} not found'


def calculate_time_in_future(hours, minutes):
    future_time = arrow.now().shift(hours=hours, minutes=minutes).format('hh:mm A')
    return f'The time in {hours} hours and {minutes} minutes will be {future_time}'


def calculate_time_difference(time1, time2):
    try:
        time1 = arrow.get(time1, 'hh:mm A')
        time2 = arrow.get(time2, 'hh:mm A')
        time_difference = time1 - time2
        return f'The difference between {time1.format("hh:mm A")} and {time2.format("hh:mm A")} is {time_difference}'
    except arrow.parser.ParserError:
        return "Invalid time format"


def handle_command():
    print('Time assistant')
    tts.speak('Time assistant')

    print('What would you like to know?')
    tts.speak('What would you like to know?')

    intent = nlp.extract_intent(srutils.recognize())

    print(intent)

    if intent == 'current time':
        response = get_current_time()
        print(response)
        tts.speak(response)
    elif intent == 'current date':
        response = get_current_date()
        print(response)
        tts.speak(response)
    elif intent == 'current day of the week':
        response = get_day_of_week()
        print(response)
        tts.speak(response)
    elif intent == 'time in location':
        if parameters and 'location' in paramets:
            location = parameters['location']
            response = get_time_in_timezone(location)
            print(response)
            tts.speak(response)
        else:
            print("Please provide a location")
            tts.speak("Please provide a location")
    elif intent == 'time in the future':
        if parameters and 'hours' in parameters and 'minutes' in parameters:
            hours = parameters['hours']
            minutes = parameters['minutes']
            response = calculate_time_in_future(hours, minutes)
            print(response)
            tts.speak(response)
        else:
            print("Please provide hours and minutes")
            tts.speak("Please provide hours and minutes")
    elif intent == 'time difference':
        if parameters and 'time1' in parameters and 'time2' in parameters:
            time1 = parameters['time1']
            time2 = parameters['time2']
            response = calculate_time_difference(time1, time2)
            print(response)
            tts.speak(response)
        else:
            print("Please provide two times")
            tts.speak("Please provide two times")
