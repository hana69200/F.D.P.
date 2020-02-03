from sense_hat import SenseHat
from time import sleep
import pygame
from pygame.locals import *


class AccelerationManager:

    def __init__(self):
        self.__hat = SenseHat()
        self.__currentShade = [50,50,50]
        self.__hat.low_light = False
    
    def getCurrentAcceleration(self):
        acceleration = self.__hat.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        print("*** ACCELEROMETER : x={0}, y={1}, z={2} ***".format(x, y, z))
        return (x, y, z)


    def getCurrentAccelerationLevel(self):
        x1, y1, z1 = self.getCurrentAcceleration()
        sleep(0.3)
        x, y, z = self.getCurrentAcceleration()
        xDiff = (abs(x) - abs(x1))
        yDiff = (abs(y) - abs(y1))
        zDiff = (abs(z) - abs(z1))
        maxDiff = max(xDiff, yDiff, zDiff) # greatest diff
        minDiff = min(xDiff, yDiff, zDiff) # smallest diff (max abs value of the negative values = decelerations)
        if (abs(maxDiff) >= abs(minDiff)) : 
            maxGap = maxDiff  # maxGap is the biggest acceleration OR deceleration (if negative)
        else :
            maxGap = minDiff
        print("*** *** ACCELERATION LEVEL : {0} *** ***\n\n".format(maxGap))
        return maxGap
    
    
    def setCurrentShade(self):
        firstAccLevel = self.getCurrentAccelerationLevel()
        sleep(0.05)
        secAccLevel = self.getCurrentAccelerationLevel()
        if (secAccLevel > firstAccLevel and abs(secAccLevel-firstAccLevel) > 0.006):
            if (self.__currentShade[1] == 0):  # green at 0, wasn't in acceleration
                self.__currentShade = [0, 40, 0]  # default green
            else : 
                if (self.__currentShade[1] < 255 - 50):  # if we can increment the green, we do
                    self.__currentShade[1] += 50
                else :
                    self.__currentShade[1] = 255

        elif (secAccLevel < firstAccLevel and abs(secAccLevel-firstAccLevel) > 0.006):
            if (self.__currentShade[0] == 0): 
                self.__currentShade = [40, 0, 0]
            else : 
                if (self.__currentShade[0] < 255 - 50):
                    self.__currentShade[0] += 50
                else :
                    self.__currentShade[0] = 255
        # Else -> we don't change the color, acceleration level constan
        else:
            self.__currentShade = [40,40,40]


    def displayAccelerationMode(self):
        pygame.init()
        pygame.display.set_mode((2, 2))
        
        running = True
        while(running):
            self.setCurrentShade()
            pixels = self.__hat.get_pixels()
            for i in range(64):
                pixels[i] = self.__currentShade
            self.__hat.set_pixels(pixels)
            self.__hat.clear(self.__currentShade)
            sleep(0.05)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_DOWN or event.key == K_UP or event.key == K_LEFT or event.key == K_RIGHT:  
                        running = False
                        print("BYE BYE")
                if event.type == QUIT:
                    running = False
                    print("BYE")


    

