#!/bin/bash
#
cat /proc/bus/input/devices

# hexdump /dev/input/event3
evtest /dev/input/event3
