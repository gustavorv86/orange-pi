#!/bin/bash
#

DEFAULT_DEV=/dev/ttyUSB0
DEFAULT_BAUD=115200

if [[ ${1} ]] && [[ ${1} == "-h" ]] || [[ ${1} == "-help" ]] || [[ ${1} == "--h" ]] || [[ ${1} == "--help" ]]; then
	echo "USAGE: "${0}" <DEVICE> <BAUDRATE>"
	exit 0
fi

if [[ ${1} ]]; then
	DEFAULT_DEV=${1}
fi

if [[ ${2} ]]; then
        DEFAULT_BAUD=${2}
fi


#cu -l ${DEFAULT_DEV} -s ${DEFAULT_BAUD}
#screen ${DEFAULT_DEV} ${DEFAULT_BAUD}
picocom -b ${DEFAULT_BAUD} ${DEFAULT_DEV}
