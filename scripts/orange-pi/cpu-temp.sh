#!/bin/bash

# cat /etc/armbianmonitor/datasources/soctemp
cat /sys/devices/virtual/thermal/thermal_zone0/temp
armbianmonitor -m
