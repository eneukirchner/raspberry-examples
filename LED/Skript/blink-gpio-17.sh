#!/bin/bash

gpio -g mode 17 out
sleep 1
while true ; do
	gpio -g write 17 1
	sleep 1
	gpio -g write 17 0
	sleep 1
done



