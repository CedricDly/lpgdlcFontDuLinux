#!/usr/bin/env python
#-*-coding: utf-8-*-

import RPi.GPIO as GPIO
import time, re

# Pattern to recognize valid commands
# MOVE
PATTERN_MOVE = "\s*MOVE\s*(-?\d*)"

# Manufacturer data
# Recommended frequency
FREQ = 50

# Go to 0 position
INIT = 7.5

# Go to minimum position
MINI = 5.0

# Go to maximum position
MAXI = 10.0

# Pin's number
SERVO_PIN = 11

# Artificial delay between commands
# That lets time to the servo to perform the action
DELAY = 0.5

# Disabling warnings
GPIO.setwarnings(False)

# GPIO mode board == number of the pin, not the gpio
GPIO.setmode(GPIO.BOARD)

# Initialisation
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Creating the PWM
pwm = GPIO.PWM(SERVO_PIN, FREQ)
pwm.start(INIT)
time.sleep(DELAY)

def angle2perc(angle):
	"""
	Return the percentage of the duty cycle corresponding to the corresponding angle.
	"""
	return ((MAXI - MINI) / 90) * angle + INIT

def changeCycle(command):
	"""
	Update the duty cycle of the pwm with the command string.
	The available commands are :
		- MOVE{Angle} (Angle can be negative).
	"""
	# Searching for the pattern in the command string
	match = re.match(PATTERN_MOVE, command).group(1)

	# If something is found, run the command
	if match:
		angle = float(match.group(1))
		pwm.ChangeDutyCycle(angle2perc(angle))
		time.sleep(DELAY)

	# Else, raising an error
	else:
		raise InvalidServoCommand("Invalid command : '{}'".format(command))

def stopPWM():
	"""
	Clean close for the pwm.
	"""
	# Stop sending value to output
	pwm.stop()

	# Release channels
	GPIO.cleanup()

class InvalidServoCommand(Exception):
	"""
	Error class to be raised when an invalid command is issued.
	"""
	pass
