import speech_recognition as sr


def recognize():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as mic:
            r.adjust_for_ambient_noise(mic, duration=1.0)
            print('Listening...')
            audio = r.listen(mic, timeout=5, phrase_time_limit=5)
            print("Processing...")
            text = r.recognize_google(audio)
            text = text.lower()
            print(f'You said: {text}')
            return text
    except sr.UnknownValueError:
        print('Sorry, I did not get that')
    except sr.RequestError as e:
        print(f'Sorry, my speech service is down {e}')
    except sr.WaitTimeoutError:
        print("Timeout: No speech detected")
