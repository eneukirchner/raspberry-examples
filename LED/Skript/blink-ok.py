#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
import sys

OK_LED = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(OK_LED, GPIO.OUT)
with open('/sys/class/leds/led0/trigger', 'w') as f:
        f.write('none')

while 1:
	try:
		GPIO.output(OK_LED, GPIO.LOW)
		sleep(1)
		GPIO.output(OK_LED, GPIO.HIGH)
		sleep(1)
	except KeyboardInterrupt:
		GPIO.cleanup()
                with open('/sys/class/leds/led0/trigger', 'w') as f:
                    f.write('mmc0')
		sys.exit()




