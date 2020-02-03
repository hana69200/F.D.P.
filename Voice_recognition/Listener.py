import speech_recognition as sr
import importlib
import traceback

execfile("./Speaking/Speaker.py")

class Listener:

    def __init__(self):
        self.__recognizer = sr.Recognizer()


    def transcribe(self):
        mic = sr.Microphone()
        with mic as source:
            #self.__recognizer.adjust_for_ambient_noise(source) # remove if problems
            print("Adjusted !")
            audio = self.__recognizer.listen(source)
            print("Listened")

            speaker = Speaker()
            try:
                transcription = self.__recognizer.recognize_google(audio)
                return transcription
            except Exception as e:
                speaker.speak("Couldn't transcribe audio")
                traceback.print_exc()
                print(e)
                return ''


