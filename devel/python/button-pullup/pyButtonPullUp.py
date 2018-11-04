#!/usr/bin/env python3

import os
import time

PIN_EXPORT = "/sys/class/gpio/export"
PIN_UNEXPORT = "/sys/class/gpio/unexport"
PIN_DIRECTION = "/sys/class/gpio/gpio{}/direction"
PIN_VALUE = "/sys/class/gpio/gpio{}/value"

# Pullup only on PC3 and PC4 (Not supported in Orange Pi Zero)
PC3 = 67


def main():

	pc3_direction = PIN_DIRECTION.format(PC3)
	pc3_value = PIN_VALUE.format(PC3)

	if not os.path.isfile(pc3_direction):
		fd = open(PIN_EXPORT, "w")
		fd.write(str(PC3));
		fd.close()

	fd = open(pc3_direction, "w")
	fd.write("in");
	fd.close()

	fd = open(pc3_value, "r")
	old_status = fd.read(1)
	fd.seek(0)

	new_status = old_status

	try:
		while 1:
			
			new_status = fd.read(1)
			fd.seek(0)

			# print("Old status: {}  New status: {}".format(old_status, new_status))

			if new_status != old_status:
				if new_status == "0":
					print("Putton is pressed")
				else:
					print("Button is released")

			old_status = new_status
			time.sleep(0.050)

	except KeyboardInterrupt:
		print("Keyboard interrupt...")
		pass

	fd = open(PIN_UNEXPORT, "w")
	fd.write(str(PC3));
	fd.close()


	print("Done")
	return


if __name__ == "__main__":
	main()
