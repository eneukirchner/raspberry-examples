#!/usr/bin/python
import smbus
import time
import math
import datetime

bus = smbus.SMBus (1) # Rev 2 Pi 1

offset = 2048
a = ""

rXMSB = ""
rXLSB = ""

rYMSB = ""
rYLSB = ""

DEVICE = 0x30 # Geraete Adresse 1D (30)
CONTROL = 0x00 # Steuerregister

XMSB = 0x01
XLSB = 0x02
YMSB = 0x03
YLSB = 0x04

# set / reset coil
bus.write_byte_data (DEVICE,CONTROL,0x00)
bus.write_byte_data (DEVICE,CONTROL,0x02)
time.sleep(0.1)

bus.write_byte_data (DEVICE,CONTROL,0x00)
bus.write_byte_data (DEVICE,CONTROL,0x04)
time.sleep(0.1)


while 1:
	bus.write_byte_data (DEVICE,CONTROL,0x00) # Reset des Geraetes
	time.sleep(0.1)

	bus.write_byte_data (DEVICE,CONTROL,0x01) # set des Geraetes
	time.sleep(0.1)

	bus.write_byte_data (DEVICE,CONTROL,0x00) # TM (take measurement)
	time.sleep(0.1)

	a = bus.read_byte_data (DEVICE,CONTROL)

	rXMSB = bus.read_byte_data (DEVICE,XMSB)
	rXLSB = bus.read_byte_data (DEVICE,XLSB)

	rYMSB = bus.read_byte_data (DEVICE,YMSB)
	rYLSB = bus.read_byte_data (DEVICE,YLSB)

	x = rXMSB*256+rXLSB-offset
	y = rYMSB*256+rYLSB-offset
#	print("%d %d" % (x,y))
	angle = math.atan2(y,x)*180.0/math.pi
        angle = angle if  angle >= 0 else angle + 360.0
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        print st + ' ' + repr(round(angle,1))

	time.sleep(1)

