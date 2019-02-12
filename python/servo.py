#!/usr/bin/env python
#-*-coding: utf-8-*-

import RPi.GPIO as GPIO
import time

# Manufacturer data
# Recommended frequency
freq 		= 50

# Go to 0 position
init 		= 7.5

# Go to minimum position
mini 		= 5.0

# Go to maximum position
maxi 		= 10.0

# Pin's number
servoPin 	= 11

# Artificial delay between commands
# That lets time to the servo to perform the action
DELAY 		= 0.5

# Disabling warnings
GPIO.setwarnings(False)

# GPIO mode board == number of the pin, not the gpio
GPIO.setmode(GPIO.BOARD)

# Initialisation
GPIO.setup(servoPin, GPIO.OUT)

# Creating the PWM
pwm = GPIO.PWM(servoPin, freq)
pwm.start(init)
time.sleep(DELAY)

def angle2perc(angle):
	"""
	Return the percentage of the duty cycle corresponding to the required angle.
	"""
 return ((maxi - mini) / 90) * angle + init

def changeCycle(command):
	"""
	Update the duty cycle of the pwm with the command string.
	The available commands are :
		- MOVE{Angle} (Angle can be negative).
	"""
	angle = float(command[4:])
	pwm.ChangeDutyCycle(angle2perc(angle))
	time.sleep(DELAY)

def stopPWM():
	"""
	Clean close for the pwm.
	"""
	# Stop sending value to output
	pwm.stop()

	# Release channel
	GPIO.cleanup()