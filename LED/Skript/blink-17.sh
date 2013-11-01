#!/bin/bash
LED=17

control_c()
{
        echo "$LED" > /sys/class/gpio/unexport
		echo "Stopped"
		exit $?
}

trap control_c SIGINT

echo "$LED" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio${LED}/direction

while true ; do
	echo 0 >/sys/class/gpio/gpio${LED}/value
	sleep 1
	echo 1 >/sys/class/gpio/gpio${LED}/value
	sleep 1
done



