#!/usr/bin/env python3

import os
import select
import time

PIN_EXPORT = "/sys/class/gpio/export"
PIN_UNEXPORT = "/sys/class/gpio/unexport"
PIN_DIRECTION = "/sys/class/gpio/gpio{}/direction"
PIN_EDGE = "/sys/class/gpio/gpio{}/edge"
PIN_VALUE = "/sys/class/gpio/gpio{}/value"

# Only PA_EINT[21:0] and PG_EINT[13:0] support interrupts
PIN = 6 # PA6

def main():

	pin_direction = PIN_DIRECTION.format(PIN)
	pin_edge = PIN_EDGE.format(PIN)
	pin = PIN_VALUE.format(PIN)
	
	if os.path.isfile(pin_direction):
		fd = open(PIN_UNEXPORT, "w")
		fd.write(str(PIN));
		fd.close()

	fd = open(PIN_EXPORT, "w")
	fd.write(str(PIN));
	fd.close()

	fd = open(pin_direction, "w")
	fd.write("in");
	fd.close()

	fd = open(pin_edge, "w")
	fd.write("rising") # none, rising, falling, both
	fd.close()

	fd = open(pin, "r")

	poller = select.epoll()
	
	# EPOLLIN		 Available for read
	# EPOLLOUT		Available for write
	# EPOLLPRI		Urgent data for read
	# EPOLLERR		Error condition happened on the assoc. fd
	# EPOLLHUP		Hang up happened on the assoc. fd
	# EPOLLET		 Set Edge Trigger behavior, the default is Level Trigger behavior
	# EPOLLONESHOT	Set one-shot behavior. After one event is pulled out, the fd is internally disabled
	# EPOLLRDNORM	 Equivalent to EPOLLIN
	# EPOLLRDBAND	 Priority data band can be read.
	# EPOLLWRNORM	 Equivalent to EPOLLOUT
	# EPOLLWRBAND	 Priority data may be written.
	# EPOLLMSG		Ignored.

	# flags = select.EPOLLIN | select.EPOLLET
	flags = select.EPOLLET

	poller.register(fd, flags)
	poller.poll(0.1) # clean polling

	try:
		while True:
			events = poller.poll()
			for fileno, event in events:
				print("File descriptor: {}   Event type: {}".format(fileno, event))
			poller.poll(0.1) # clean polling

	except KeyboardInterrupt:
		pass

	poller.unregister(fd)
	fd.close()

	fd = open(PIN_UNEXPORT, "w")
	fd.write(str(PIN));
	fd.close()

	print("Done")
	return


if __name__ == "__main__":
	main()

