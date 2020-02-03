from gtts import gTTS
import os

class Speaker:
    """
        Speaker is a wrapper around the gtts service

        The constructor defaults in english and normal speed speaking. You can enable slow speaking or change language through the arguments.
        
        Simply use an instance of the class and its method speak() to make the program talk.
        You can simply pass a string, and you can (but musn't) pass the generated mp3 file name.
        It creates a MP3 file locally with the text converted to speach by the google servers, and plays it using the bash mpg321 mp3 player. All needed dependencies are listed in install_dependencies.sh.
        The generated MP3 file is deleted after playing for memory management purposes.
    """
    def __init__(self, lang='en', slow_speaking=False):  # lang defaults to english, slow speaking to false
        self._lang = lang
        self._slow_speaking = slow_speaking


    def speak(self, text, output_file="speaking.mp3"):
        ttsInstance = gTTS(text=text, lang=self._lang, slow=self._slow_speaking)

        if (output_file[-4:] != '.mp3'):  # checks 4 last chars
            output_file += '.mp3'

        ttsInstance.save(output_file)  # creates the mp3 file
        os.system("mpg321 " + output_file)  # Uses a lightweight CLI mp3 player - is included in the dependencies script
        os.system("rm ./" + output_file)  # cleaning up

# Example of using : 
    # inst = Speaker()
    # inst.speak("Hello Ugo how are you? I am the f.d.p.")