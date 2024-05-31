mport speech_recognition as sr

def asr_sr():
    init_rec = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio_data = init_rec.record(source, duration=1.5)
            text = init_rec.recognize_google(audio_data, language='en-UK').lower()
            print(f"Recognized command: {text}")
            return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ''
    except sr.RequestError as e:
        print(f"Could not request results; check your internet connection. Error: {e}")
        return ''
