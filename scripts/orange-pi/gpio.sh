#!/bin/bash

###### ORANGE PI PINES ######

PIN=(PA0 PA1 PA2 PA3 PA4 PA5 PA6 PA7 PA8 PA9 PA10 PA11 PA12 PA13 PA14 PA18 PA19 PA20 PA21 PC0 PC1 PC2 PC3 PC4 PC7 PD14 PG6 PG7 PG8 PG9)
PHY=(0   1   2   3   4   5   6   7   8   9   19   11   12   13   14   18   19   20   21   64  65  66  67  68  71  110  198 199 200 201)

help(){
	echo "USAGE: "
	echo -e " \t "${0}" pinout"
	echo -e " \t "${0}" PXNN mode [in|out]"
	echo -e " \t "${0}" PXNN write [1|0]"
	echo -e " \t "${0}" PXNN read"
	echo
}

indexof() {
	local pin_array=("${!1}")
	local pin=${2}

	for i in "${!pin_array[@]}"; do
		if [ "${pin_array[$i]}" == "${pin}" ]; then
			echo ${i}
			return 1
		fi
	done
	echo "-1"
	return 0
}

pinout() {
	local pin_array=("${!1}")
	local phy_array=("${!2}")

	echo -e "PIN \t PHY \t MODE \t VALUE"
	for i in "${!pin_array[@]}"; do
		pin="${pin_array[$i]}"
		phy="${phy_array[$i]}"
		if [ -d /sys/class/gpio/gpio${phy} ]; then
			mode=$(cat /sys/class/gpio/gpio${phy}/direction)
			value=$(cat /sys/class/gpio/gpio${phy}/value)
                else
			mode="   "
                        value="unexport"
                fi

		echo -e ${pin}" \t "${phy}" \t "${mode}" \t "${value}
        done
}

pin_mode() {
	local phy=${1}
	local mode=${2}
	if [ ! -d /sys/class/gpio/gpio${phy} ]; then
		echo ${phy} > /sys/class/gpio/export
	fi

	echo ${mode} > /sys/class/gpio/gpio${phy}/direction
}

pin_read() {
	local phy=${1}

	if [ ! -d /sys/class/gpio/gpio${phy} ]; then
		echo "Unexport pin"
		return 0
	fi

	cat /sys/class/gpio/gpio${phy}/value
	return 1
}

pin_write() {
	local phy=${1}
	local value=${2}

	if [ ! -d /sys/class/gpio/gpio${phy} ]; then
		echo "Unexport pin"
		return 0
        fi

	echo ${value} > /sys/class/gpio/gpio${phy}/value
	return 1
}


####################################################
################        MAIN        ################
####################################################

if [ ${#} -eq 0 ]; then
	help
	exit 0
fi

if [ ${1} == "-h" ] || [ ${1} == "help" ] || [ ${1} == "-help" ] || [ ${1} == "--help" ]; then
        help
        exit 0
fi

if [ ${#} -eq 1 ] && [ ${1} == "pinout" ]; then
	pinout PIN[@] PHY[@]
	exit 0
fi

if [ ${#} -lt 2 ]; then
	echo "Invalid number of arguments"
	exit 0
fi

pin=${1}
index=$(indexof PIN[@] ${pin})

if [ ${index} -eq -1 ]; then
	echo "Pin not found"
	exit 0
fi

phy=${PHY[${index}]}
opt=${2}

if [ ${opt} == "mode" ]; then

	if [ ${#} -eq 3 ]; then
		pin_mode ${phy} ${3}
	else
		echo "Invalid number of parameters"
	fi

elif [ ${opt} == "write" ]; then

	if [ ${#} -eq 3 ]; then
		pin_write ${phy} ${3}
	else
		echo "Invalid number of parameters"
	fi

elif [ ${opt} == "read" ]; then

	pin_read ${phy}

else

	echo "Invalid argument '"${opt}

fi
