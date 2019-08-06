#!/usr/bin/python
import RPi.GPIO as GPIO

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
#Library for time delay
import time
from time import sleep

# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
vcc_motor = GPIO.PWM(15, 60) # Frecuencia 60Hz

pause_time =  0.2

vcc_motor.start(0)

# blinking function
def blink(pin1, pin2):
        GPIO.output(pin1,GPIO.HIGH)
        GPIO.output(pin2,GPIO.LOW)
        time.sleep(5)
        GPIO.output(pin2,GPIO.HIGH)
        GPIO.output(pin1,GPIO.LOW)
        time.sleep(5)
        return

while True:
        for i in range(0,101, 10):
            vcc_motor.ChangeDutyCycle(i)
            sleep(pause_time)
            blink(11,8)
        for i in range(100, -1, -10):
            vcc_motor.ChangeDutyCycle(i)
            sleep(pause_time)
            blink(11,8)



GPIO.cleanup()

