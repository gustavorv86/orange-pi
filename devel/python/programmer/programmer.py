#!python

#### IMPORTS ####

import datetime
import os
import os.path
import time
import RPi.GPIO as GPIO

#### CONSTANTES ####

FILENAME = "/home/pi/commands/programmer/time.txt"
TIME_SLEEP = (5 * 60)  # 5 minutos
PIN = 1
GPIO_ON = GPIO.LOW    # encendido a nivel bajo
GPIO_OFF = GPIO.HIGH  # apagado a nivel alto

#### FUNCIONES ####

def gpio(level):
    GPIO.setmode(GPIO.BOARD)   # GPIO.BCM or GPIO.BOARD
    GPIO.setup(PIN, GPIO.OUT)  # GPIO PIN como salida
    GPIO.output(PIN, level)    # PIN a nivel alto
    return


def time_minor(t_time1, t_time2):
    if (t_time1["hour"] > t_time2["hour"]):
        return False
    elif (t_time1["hour"] == t_time2["hour"]):
        if (t_time1["minute"] > t_time2["minute"]):
            return False
        elif (t_time1["second"] > t_time2["second"]):
            return False

    return True


def time_now():
    now_time = datetime.datetime.now().time()
    t_time = {}
    t_time["hour"] = now_time.hour
    t_time["minute"] = now_time.minute
    t_time["second"] = now_time.second
    return t_time


def time_in_seconds(t_time):
    return (t_time["hour"]*60*60) + (t_time["minute"]*60) + t_time["second"]


def time_list_check(time_list):
    for i in range(1, len(time_list)):
        if not time_minor(time_list[i-1], time_list[i]):
            return False

    return True


def time_list_check_status(time_list, t_time):
    for i in range(1, len(time_list)):
        sec_min = time_in_seconds(time_list[i-1])
        sec     = time_in_seconds(t_time);
        sec_max = time_in_seconds(time_list[i])

        if(sec_min <= sec and sec < sec_max) :
            return time_list[i-1]["stat"]

    return time_list[len(time_list)-1]["stat"]


def read_file():
    if not os.path.isfile(FILENAME):
        print("FILE NOT FOUND...")
        return []
    
    time_list = []
    with open(FILENAME) as file:
        for line in file:
            trim_line = line.strip()
            if trim_line:
                args = trim_line.split()
                args_time = args[0].split(":")
                t_time = {}
                t_time["hour"] = int(args_time[0])
                t_time["minute"] = int(args_time[1])
                t_time["second"] = int(args_time[2])
                t_time["stat"] = args[1].upper() == "ON"
                time_list.append(t_time)

    if not time_list_check(time_list):
        print("INPUT DATA FILE ERROR...")
        return []

    return time_list


def main():
    print("Start program")
    print(os.getcwd())
    while (True):
        now_time = time_now()
        time_list = read_file()
        if time_list:
            now_time = time_now()
            val = time_list_check_status(time_list, now_time)
            if (val == True):
                s = str(now_time["hour"])+":"+str(now_time["minute"])+":"+str(now_time["second"])+" ON"
                print(s)
                # gpio(GPIO_ON)
            else:
                s = str(now_time["hour"])+":"+str(now_time["minute"])+":"+str(now_time["second"])+" OFF"
                print(s)
                # gpio(GPIO_OFF)
        # end_if
        time.sleep(TIME_SLEEP)
    # end_while
    return


main()

