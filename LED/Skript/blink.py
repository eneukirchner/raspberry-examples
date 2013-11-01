#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

OK_LED = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(OK_LED, GPIO.OUT)
sleep(1)

while 1:
	GPIO.output(OK_LED, GPIO.LOW)
	sleep(1)
	GPIO.output(OK_LED, GPIO.HIGH)
	sleep(1)


