#!/bin/bash

if [ ${1} ]; then
	echo ${1} > /sys/class/leds/red_led/brightness
fi

