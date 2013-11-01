#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
from time import sleep

LED = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)

while 1:
    try:
	GPIO.output(LED, GPIO.LOW)
	sleep(1)
	GPIO.output(LED, GPIO.HIGH)
	sleep(1)

    except KeyboardInterrupt:
	GPIO.cleanup()
	sys.exit()



