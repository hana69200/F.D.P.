import os
from sense_hat import SenseHat


def playMusic():
    os.system("mpg321 " + "./Music/LyreLeTemps.mp3")  


    sense  = SenseHat()

    #part smiley
    sense.low_light = True
    sense.clear((0,0,0))
    sense.set_pixel(0,5,(255,255,255))
    sense.set_pixel(0,6,(255,255,255))
    sense.set_pixel(1,4,(255,255,255))
    sense.set_pixel(1,5,(255,255,255))
    sense.set_pixel(1,6,(255,255,255))
    sense.set_pixel(1,7,(255,255,255))
    sense.set_pixel(2,4,(255,255,255))
    sense.set_pixel(2,5,(255,255,255))
    sense.set_pixel(2,6,(255,255,255))
    sense.set_pixel(2,7,(255,255,255))
    sense.set_pixel(3,0,(255,255,255))
    sense.set_pixel(3,1,(255,255,255))
    sense.set_pixel(3,2,(255,255,255))
    sense.set_pixel(3,3,(255,255,255))
    sense.set_pixel(3,4,(255,255,255))
    sense.set_pixel(3,5,(255,255,255))
    sense.set_pixel(3,6,(255,255,255))
    sense.set_pixel(3,7,(255,255,255))
    sense.set_pixel(4,1,(255,255,255))
    sense.set_pixel(5,1,(255,255,255))
    sense.set_pixel(5,2,(255,255,255))
    sense.set_pixel(6,2,(255,255,255))
    sense.set_pixel(6,3,(255,255,255))
    
    
# PLAY 1 MUSIC, done : ask with the speaker if they want to play the next one or to leave, IF they say leave, YOU EXIT, else you play the next

