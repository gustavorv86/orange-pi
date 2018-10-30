#!/usr/bin/env python3

import os
import time

PIN_EXPORT = "/sys/class/gpio/export"
PIN_UNEXPORT = "/sys/class/gpio/unexport"
PIN_DIRECTION = "/sys/class/gpio/gpio{}/direction"
PIN_VALUE = "/sys/class/gpio/gpio{}/value"

PC3 = 67


def main():

	pc3_direction = PIN_DIRECTION.format(PC3)
	pc3_value = PIN_VALUE.format(PC3)

	if not os.path.isfile(pc3_direction):
		fd = open(PIN_EXPORT, "w")
		fd.write(str(PC3));
		fd.close()

	fd = open(pc3_direction, "w")
	fd.write("out");
	fd.close()

	fd = open(pc3_value, "w")

	try:
		while 1:
			print("Led ON")
			fd.write("1")
			fd.flush()
			time.sleep(1)

			print("Led OFF")
			fd.write("0")
			fd.flush()
			time.sleep(1)

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
