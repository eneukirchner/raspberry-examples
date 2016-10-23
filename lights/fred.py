#!/usr/bin/python
import os.path
file_path="/home/pi/lights/leds-on"

if os.path.exists(file_path):
	print ("File existiert!");
else:
	print ("File existiert nicht!");
	
