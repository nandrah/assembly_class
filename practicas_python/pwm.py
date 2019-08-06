#!/usr/bin/python
import RPi.GPIO as GPIO

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
#Library for time delay
import time

GPIO.setup(11, GPIO.OUT)

# to create a PWM instance: channel, frecuency
p = GPIO.PWM(11, 30) # Frecuency 30Hz, tiempo =1/30Hz

# to start PWM
p.start(1) # Duty cycle 1% (0-100)
input('Press return to stop: ')
p.stop()

GPIO.cleanup()

