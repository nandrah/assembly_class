#! usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
Led=11

GPIO.setup(Led, GPIO.OUT)

white=GPIO.PWM(Led, 100)

white.start(0) # Duty cycle = 0%

pause_time=0.02

try:
    while True:
        for i in range(0,101):
            white.ChangeDutyCycle(i)
            sleep(pause_time)
        for i in range(100, -1, -1):
            white.ChangeDutyCycle(i)
            sleep(pause_time)

except KeyboardInterrupt:
    white.stop()
    #red.stop()
    GPIO.cleanup()

