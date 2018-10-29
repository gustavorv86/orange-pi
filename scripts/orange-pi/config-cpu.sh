#!/bin/bash
#

MIN_MHZ=240
MAX_MHZ=960
GOVERNOR=conservative

CFGFILE=/etc/default/cpufrequtils

echo ">> CPU info"
echo
cpufreq-info -c 0
echo
echo

echo ">> Available governors"
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors
echo

echo ">> Available frequencies"
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies
echo

echo
echo ">> Configuring CPU"
echo

if [[ ! -f ${CFGFILE}".bak" ]];then
	cp ${CFGFILE} ${CFGFILE}".bak"
fi

echo -ne > ${CFGFILE}
echo "ENABLE=true" >> ${CFGFILE}
echo "MIN_SPEED="${MIN_MHZ}"000" >> ${CFGFILE}
echo "MAX_SPEED="${MAX_MHZ}"000" >> ${CFGFILE}
echo "GOVERNOR="${GOVERNOR} >> ${CFGFILE}
echo >> ${CFGFILE}

echo ">> Done"
echo
