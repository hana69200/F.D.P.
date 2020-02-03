from sense_hat import SenseHat

execfile("./Speaking/Speaker.py")
execfile("./Voice_recognition/Listener.py")
execfile("./Acceleration/Acceleration.py")
execfile("./Emotions/emotions.py")
execfile("./Music/test.py")



def modeSelectionLoop():
	
    sense  = SenseHat()
    sense.low_light = True
    sense.clear((0,0,0))

    speaker = Speaker()
    listener = Listener()
    looping = True

    while (looping):
        #speaker.speak('What module would you like to start? Please say one of the following words clearly and loud enough : Acceleration. Music. Emotions. Say your word in 5 seconds.')
        speaker.speak('speak in 5 seconds')
        voiceInput = listener.transcribe()

        if voiceInput.lower() == 'acceleration':
            speaker.speak('You have selected the acceleration module.')
            looping = False

            aManager = AccelerationManager()
            aManager.displayAccelerationMode()  
        elif voiceInput.lower() == 'music':
            speaker.speak('You have selected the music module.')
            looping = False
            
            playMusic()
        elif voiceInput.lower() == 'emotions' or voiceInput.lower() == 'emotion' :
            speaker.speak('You have selected the emotions module.')
            looping = False
        
            listen()
        else:
            if voiceInput != '':
                speaker.speak('Invalid input. You have said :')
                speaker.speak(voiceInput)
            speaker.speak('Please try again.')
        
def main():
    listener = Listener()
    speaker = Speaker()
    speaker.speak('Hi ! I\'m your funny driving partner! Let\'s hit the road! ')
    modeSelectionLoop()
    
    looping = True
    while (looping):
        speaker.speak('You have exited the current functionnality. Would you like to enter another one? (Say YES or NO in 5 seconds.) ')
        yesOrNo = listener.transcribe()
        if yesOrNo.lower() == 'yes':
            modeSelectionLoop()
        else :
            looping = False
    speaker.speak('Shutting down. See you on the next trip !')



main()
