import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak into microphone")
    audio = r.listen(source)