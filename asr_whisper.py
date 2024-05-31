import speech_recognition as sr
import whisper

def asr_whisper(asr_model):
    model = asr_model
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Recording...")
            audio = r.record(source, duration=1.5)
            with open("recording.wav", "wb+") as f:
                f.write(audio.get_wav_data())

        path = "recording.wav"
        result = model.transcribe(path, fp16=False)
        text = result['text'].lower()
        print(text)
        return text
    except sr.UnknownValueError:
        return ''
