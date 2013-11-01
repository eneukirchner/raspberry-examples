#!/bin/bash

control_c()
{
	echo "mmc0" > /sys/class/leds/led0/trigger
	exit $?
}

trap control_c SIGINT

echo "none" > /sys/class/leds/led0/trigger

while true ; do
	echo 0 >/sys/class/leds/led0/brightness
	sleep 1
	echo 1 >/sys/class/leds/led0/brightness
	sleep 1
done



