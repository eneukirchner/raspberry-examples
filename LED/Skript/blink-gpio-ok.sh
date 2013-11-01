#!/bin/bash
control_c()
{
        echo "mmc0" >/sys/class/leds/led0/trigger
        exit $?
}

trap control_c SIGINT

echo "none" >/sys/class/leds/led0/trigger

gpio -g mode 16 out
sleep 1
while true ; do
	gpio -g write 16 1
	sleep 1
	gpio -g write 16 0
	sleep 1
done



