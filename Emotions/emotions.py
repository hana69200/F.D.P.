import collections
import audioop
import pyaudio
import pygame
from pygame.locals import *
from sense_hat import SenseHat
from time import sleep
execfile("./Speaking/Speaker.py")
execfile("./Voice_recognition/Listener.py")



def listen():
    sense  = SenseHat()
    pygame.init()
    pygame.display.set_mode((2, 2))
    
    w = (255,255,255)
    b = (0,0,0)
    
    smiley_angry = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,w,w,b,b,w,w,b,
        b,w,w,b,b,w,w,b,
        b,b,b,b,b,b,b,b,
        b,b,w,w,w,w,b,b,
        b,w,b,b,b,b,w,b,
        w,b,b,b,b,b,b,w
    ]
    
    smiley_happy = [
        b,b,b,b,b,b,b,b,
        b,b,w,b,b,w,b,b,
        b,b,w,b,b,w,b,b,
        b,b,w,b,b,w,b,b,
        b,b,b,b,b,b,b,b,
        w,b,b,b,b,b,b,w,
        b,w,b,b,b,b,w,b,
        b,b,w,w,w,w,b,b
    ]
    
    music_note = [
        b,b,b,w,b,b,b,b,
        b,b,b,w,w,w,b,b,
        b,b,b,w,b,w,w,b,
        b,b,b,w,b,b,w,b,
        b,w,w,w,b,b,b,b,
        w,w,w,w,b,b,b,b,
        w,w,w,w,b,b,b,b,
        b,w,w,w,b,b,b,b,
    ]
    
    
    CHUNK = 256 # number of frames per buffer
    FORMAT = pyaudio.paInt16 # audio format (16 bit)
    CHANNELS = 1 # number of channel (1 = mono)
    DEV_INDEX = pyaudio.PyAudio().get_default_input_device_info().get('index') # Return the index of default input device
    RATE = 44100 # The sample rate for audio in Hz99
    RECORD_SECONDS=1 

    
    p = pyaudio.PyAudio() #create a new stream
    
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print 'Input Device id ', i, ' - ', p.get_device_info_by_host_api_device_index(0, i).get('name')
            DEV_INDEX = p.get_device_info_by_host_api_device_index(0, i).get('index')
            print('SELECTED INDEX : {}'.format(DEV_INDEX))

    
    q = collections.deque(maxlen=(int)(RATE/CHUNK)) #make a stack(pile) with a maximum size about the number of possible records

    print("--Listening--")
    running = True
    
    while(running):
        stream = p.open(format=FORMAT, channels=CHANNELS,rate=RATE,input=True, frames_per_buffer=CHUNK, input_device_index=DEV_INDEX) #open the stream
        data = stream.read(CHUNK) #read 1024 frames
        stream.close()
        q.append(abs(audioop.avg(data,4)))
        if (sum(q)/(RATE/CHUNK*RECORD_SECONDS)>70000000):
            print('too high')
            sense.set_pixels(smiley_angry)
        else:
            print('not too high')
            sense.set_pixels(smiley_happy)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_DOWN or event.key == K_UP or event.key == K_LEFT or event.key == K_RIGHT:  
                    running = False
                    print("BYE BYE")
            if event.type == QUIT:
                running = False
                print("BYE")
            
        




