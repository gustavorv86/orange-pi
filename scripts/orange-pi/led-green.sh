#!/bin/bash

if [ ${1} ]; then
	echo ${1} > /sys/class/leds/green_led/brightness
fi

