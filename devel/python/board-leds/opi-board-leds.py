#!/usr/bin/python

import os
import threading
import time

LED_GREEN = "/sys/class/leds/green_led/brightness"
LED_RED   = "/sys/class/leds/red_led/brightness"

def board_led_get_value(led) :
	if not os.path.isfile(led) :
		print("ERROR: device not found")
		return -1

	fd = open(led, "r")
	strvalue = fd.readline().strip()
	fd.close()
	return int(strvalue)



def board_led_set_value(led, value) :
	if not os.path.isfile(led) :
		print("ERROR: device not found")
		return False

	fd = open(led, "w")
	if value == 0 or value == "0" or value == False :
		fd.write("0")
	else :
		fd.write("1")
	fd.close()
	return True



class board_led_blink(threading.Thread) :
	
	def __init__(self, led, initValue, millisOn, millisOff):
		threading.Thread.__init__(self)
		self.led = led
		self.initValue = initValue
		self.millisOn = millisOn
		self.millisOff = millisOff
		self.running = True

	def run(self) :
		board_led_set_value(self.led, self.initValue)
		while(self.running) :
			value = board_led_get_value(self.led)
			if value == 0 :
				board_led_set_value(self.led, 1)
				time.sleep(float(self.millisOn) / 1000)			
			else :
				board_led_set_value(self.led, 0)
				time.sleep(float(self.millisOff) / 1000)

	def stop(self) :
		self.running = False


def main() :

	red_thread = board_led_blink(LED_RED, 1, 500, 250)
	green_thread = board_led_blink(LED_GREEN, 0, 250, 500)

	print("Start threads...")    
	green_thread.start()
	red_thread.start()

	time.sleep(15)

	print("Stopping threads...")
	green_thread.stop()
	red_thread.stop()

	green_thread.join()
	red_thread.join()

	board_led_set_value(LED_RED, 0)
	board_led_set_value(LED_GREEN, 0)

	print("Done")

main()

