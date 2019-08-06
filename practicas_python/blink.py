#!/usr/bin/python
import RPi.GPIO as GPIO

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
#Library for time delay
import time

# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.IN)

# blinking function
def blink(pin1, pin2):
        GPIO.output(pin1,GPIO.HIGH)
        GPIO.output(pin2,GPIO.LOW)
        time.sleep(1)
        GPIO.output(pin2,GPIO.HIGH)
        GPIO.output(pin1,GPIO.LOW)
        time.sleep(1)
        return

# blink GPIO17 50 times
for i in range(0,2):
        blink(11,8)

# read pin10
pin10 = GPIO.input(10)

if pin10==1:
        for i in range(0,10):
                blink(11,8)
else:
        print "No se activo"

print pin10

GPIO.cleanup()

