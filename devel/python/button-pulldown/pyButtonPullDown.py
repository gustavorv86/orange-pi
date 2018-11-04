#!/usr/bin/env python3

import os
import time

PIN_EXPORT = "/sys/class/gpio/export"
PIN_UNEXPORT = "/sys/class/gpio/unexport"
PIN_DIRECTION = "/sys/class/gpio/gpio{}/direction"
PIN_VALUE = "/sys/class/gpio/gpio{}/value"

PA6 = 6


def main():

	pa6_direction = PIN_DIRECTION.format(PA6)
	pa6_value = PIN_VALUE.format(PA6)

	if not os.path.isfile(pa6_direction):
		fd = open(PIN_EXPORT, "w")
		fd.write(str(PA6));
		fd.close()

	fd = open(pa6_direction, "w")
	fd.write("in");
	fd.close()

	fd = open(pa6_value, "r")
	old_status = fd.read(1)
	fd.seek(0)

	new_status = old_status

	try:
		while 1:
			
			new_status = fd.read(1)
			fd.seek(0)

			# print("Old status: {}  New status: {}".format(old_status, new_status))

			if new_status != old_status:
				if new_status == "1":
					print("Putton is pressed")
				else:
					print("Button is released")

			old_status = new_status
			time.sleep(0.050)

	except KeyboardInterrupt:
		print("Keyboard interrupt...")
		pass

	fd = open(PIN_UNEXPORT, "w")
	fd.write(str(PA6));
	fd.close()


	print("Done")
	return


if __name__ == "__main__":
	main()

