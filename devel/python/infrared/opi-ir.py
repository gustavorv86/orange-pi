#!/usr/bin/python

# cat /proc/bus/input/devices
DEV_IR_EVENT = "/dev/input/event3"

def main() :
	fd = open(DEV_IR_EVENT, "r")
	
	while True :
		read = fd.read()
		# convert read to hex
		print("Length: (" + str(read) + "): " + read)






main()
