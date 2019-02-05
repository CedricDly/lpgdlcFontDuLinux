#!/usr/bin/env python
#-*-coding: latin-1-*-

import RPi.GPIO as GPIO
import time

init = 7.5
mini = 5.0
maxi = 10.0
DELAY = 0.5 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
servoPin = 11
GPIO.setup(servoPin,GPIO.OUT)
pwm = GPIO.PWM(servoPin, 50)
pwm.start(init)
time.sleep(DELAY)

def angle2perc(angle):
 return ((maxi - mini) / 90) * angle + init

def changeCycle(string):
	angle = float(string[4:])
	pwm.ChangeDutyCycle(angle2perc(angle))
	time.sleep(DELAY)

def stopPWM():
	pwm.stop() #stop sending value to output
	GPIO.cleanup() #release channel
