
import pyaudio
pyaudio.__version__


import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")
'''
from PyQt5.Qt import PYQT_VERSION_STR
print("PyQt version:", PYQT_VERSION_STR)
'''