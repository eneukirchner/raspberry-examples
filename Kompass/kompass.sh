#!/bin/bash
# modprobe i2c-bcm2708
# modprobe i2c-dev 

offset=2048

# set coil
i2cset -y 1 0x30 0x00
i2cset -y 1 0x30 0x02
sleep 0.1
#reset coil
i2cset -y 1 0x30 0x00
i2cset -y 1 0x30 0x04
sleep 0.1

#endles loop, get data
while [ 1 -eq 1 ]
	do
	i2cset -y 1 0x30 0x00
	i2cset -y 1 0x30 0x00 0x01
	sleep 0.1
	i2cset -y 1 0x30 0x00
	dummy=`i2cget -y 1 0x30`
	xh=$(i2cget -y 1 0x30)
	xl=$(i2cget -y 1 0x30)
	yh=$(i2cget -y 1 0x30)
	yl=$(i2cget -y 1 0x30)
	echo "X= $xh,$xl Y= $yh,$yl"
	xh=$(($xh & 0x0f))
	xl=$(($xl))	
	yh=$(($yh & 0x0f))	
	yl=$(($yl))	
	x=$(($xh*256+$xl-$offset))
	y=$(($yh*256+$yl-$offset))

	echo "$x"
	echo "$y"
	if [ $x -ne 0 ] ; then
		echo "a($y/$x)*180.0/3.14" | bc -l
	else 
		if [ $y -ge 0 ] ; then
			echo "90"
		else
			echo "-90"
		fi
	fi
done
