#!/bin/bash

gpio -g mode 16 out
sleep 1
while true ; do
	gpio -g write 16 1
	sleep 1
	gpio -g write 16 0
	sleep 1
done



