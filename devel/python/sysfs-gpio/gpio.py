#!/usr/bin/env python

import os
import sys

PINOUT_OPI = [
	("PA0"  , 0),
	("PA1"  , 1),
	("PA2"  , 2),
	("PA3"  , 3),
	("PA4"  , 4),
	("PA5"  , 5),
	("PA6"  , 6),
	("PA7"  , 7),
	("PA8"  , 8),
	("PA9"  , 9),
	("PA10" , 10),
	("PA11" , 11),
	("PA12" , 12),
	("PA13" , 13),
	("PA14" , 14),
	("PA18" , 18),
	("PA19" , 19),
	("PA20" , 20),
	("PA21" , 21),
	("PC0"  , 64),
	("PC1"  , 65),
	("PC2"  , 66),
	("PC3"  , 67),
	("PC4"  , 68),
	("PC7"  , 71),
	("PD14" , 110),
	("PG6"  , 198),
	("PG7"  , 199),
	("PG8"  , 200),
	("PG9"  , 201)
]

PINOUT_OPI_ZERO = [
	("PA0"  , 0),
	("PA1"  , 1),
	("PA2"  , 2),
	("PA3"  , 3),
	("PA6"  , 6),
	("PA7"  , 7),
	("PA10" , 10),
	("PA11" , 11),
	("PA12" , 12),
	("PA13" , 13),
	("PA14" , 14),
	("PA15" , 15),
	("PA16" , 16),
	("PA18" , 18),
	("PA19" , 19),
	("PG6"  , 198),
	("PG7"  , 199)
]



# Configure pinout Orange PI / Zero
PINOUT = PINOUT_OPI



def show_help() :
	script_name = os.path.basename(__file__)
	
	print("USAGE: ")
	print(" \t " + script_name + " readall")
	print(" \t " + script_name + " mode PXNN [in|out]")
	print(" \t " + script_name + " write PXNN [1|0]")
	print(" \t " + script_name + " read PXNN")
	print
	return True



def readall() :
	print("PIN \t PHY \t MODE \t VALUE")
	print("============================================")
		
	for pin_tuple in PINOUT :
		strphy = str(pin_tuple[1])
		mode = "none"
		value = ""
		if os.path.isdir("/sys/class/gpio/gpio" + strphy) :
			fdesc = open("/sys/class/gpio/gpio" + strphy + "/direction", "r")
			mode = fdesc.readline().strip()
			fdesc.close()

			fdesc = open("/sys/class/gpio/gpio" + strphy + "/value", "r")
			value = fdesc.readline().strip()
			fdesc.close()

		print(pin_tuple[0] + " \t " + strphy + " \t " + mode + " \t " + value)
		
	return True
	


def pin_to_phy(pin) :
	
	for pin_tuple in PINOUT :
		if pin_tuple[0] == pin :
			return pin_tuple[1]
		
	return -1



def pin_mode(pin, mode, value=0) :
	phy = pin_to_phy(pin)
	if phy == -1 :
		print("ERROR: invalid pin")
		return False
	
	strphy = str(phy)
	
	if not os.path.isdir("/sys/class/gpio/gpio" + strphy) :
		fdesc = open("/sys/class/gpio/export", "w")
		fdesc.write(strphy);
		fdesc.close()
	
	try :
		fdesc = open("/sys/class/gpio/gpio" + strphy + "/direction", "w")
		fdesc.write(str(mode));
		fdesc.close()
		pin_write(pin, value)
		return True
	except IOError :
		print("ERROR: invalid argument")
		return False

	

def pin_read(pin) :
	phy = pin_to_phy(pin)
	if phy == -1 :
		print("ERROR: invalid pin")
		return -1
	
	strphy = str(phy)
	if not os.path.isdir("/sys/class/gpio/gpio" + strphy) :
		print("ERROR: unexport pin")
		return -1
	
	fdesc = open("/sys/class/gpio/gpio" + strphy + "/value", "r")
	strvalue = fdesc.readline().strip()
	fdesc.close()

	try :
		value = int(strvalue)
	except ValueError :
		value = -1
	return value



def pin_write(pin, value) :
	phy = pin_to_phy(pin)
	if phy == -1 :
		print("ERROR: invalid pin")
		return False

	strphy = str(phy)
	if not os.path.isdir("/sys/class/gpio/gpio" + strphy) :
		print("ERROR: unexport pin")
		return False
	
	fdesc = open("/sys/class/gpio/gpio" + strphy + "/value", "w")
	if value == 0 or value == "0" or value == False :
		fdesc.write("0")
	else :
		fdesc.write("1")
	fdesc.close()
	return True



def main() :
	
	argc = len(sys.argv)
	
	option = ""
	pin = ""
	direction = ""
	value = 0
	
	if argc >= 2 :
		option = sys.argv[1]
		
	if argc >= 3 :
		pin = sys.argv[2]


	if option == "help" or option == "--help" or option == "-h" or option == "?" :
	
		show_help()
	
	elif option == "readall" :
		
		readall()
	
	elif option == "mode" :
		
		if argc >= 4 :
			direction = sys.argv[3]

		if argc >= 5 :
			value = sys.argv[4]

		pin_mode(pin, direction, value)

	elif option == "read" :
	
		value = pin_read(pin)
		if value != -1 :
			print(value)
		
	elif option == "write" :
		
		if argc >= 4 :
			value = sys.argv[3]

		pin_write(pin, value)
		
	else :
		
		print("ERROR: invalid command")
	
	return True


main()

