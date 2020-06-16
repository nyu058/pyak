"""
A boring project during covid-19
Works with slack 
"""


import re
import os
import sys
import time
import psutil
import logging
import argparse
import platform
import pyautogui
import subprocess
from datetime import datetime


#todo windows logging support
if platform.system() == "Windows":
   logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S')

else: 
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.DEBUG,
        handlers=(logging.StreamHandler(sys.stdout), logging.FileHandler(
            "{}/Library/Logs/auto_key_{}.log".format(os.getenv("HOME"), datetime.now().strftime("%Y-%m-%d_%H:%M:%S")))),
        datefmt='%Y-%m-%d %H:%M:%S')


def auto_keypress(interval, key='shift', time_active=None, process=''):

    if time_active:
        start = datetime.strptime(time_active[0], "%H:%M").time()
        end = datetime.strptime(time_active[1], "%H:%M").time()
        logging.info("Auto key presser started. '{}' key will be pressed for every {} seconds between {} and {}".format(
            key, interval, time_active[0], time_active[1]))

    else:
        logging.info(
            "Auto key presser started. '{}' key will be pressed for every {} seconds".format(key, interval))

    sleep_time = interval
    while 1:

        time.sleep(sleep_time)
        inactive_time = get_inactive_time()

        # reset the timer if system is active
        if inactive_time < interval:
            sleep_time = interval - inactive_time
            logging.debug("Timer reset. Inactive time: {}".format(inactive_time))
            continue
        else:
            sleep_time = interval

        if not time_active or time_in_range(start, end, datetime.now().time()):
            if not process or is_process_exist(process):
                press_key(key)


def time_in_range(start, end, now):
    if start <= end:
        return start <= now <= end
    else:
        return start <= now or now <= end


def is_process_exist(process):

    regex = re.compile(process.lower())

    if list(filter(regex.match, (p.name().lower() for p in psutil.process_iter()))):
        logging.info("A process matching '{}' is running".format(process))
        return True

    return False

def get_inactive_time():
    # the value from this cmd resets ONLY if a REAL keyboard/mouse input is detected
    cmd = "/usr/sbin/ioreg -c IOHIDSystem | /usr/bin/awk '/HIDIdleTime/ {print int($NF/1000000000); exit}'"
    output = subprocess.check_output(cmd, shell=True)
    return int(output.decode("utf-8"))


def press_key(key, duration=None):

    pyautogui.press(key)
    logging.info("Pressed '{}' key".format(key))


def run():
    parser = argparse.ArgumentParser(description='Auto key presser')

    parser.add_argument('interval', type=int, metavar='SECONDS',
                        help="Interval between each key press in seconds.")
    parser.add_argument('-k', '--key', nargs='?',
                        default='shift', help="Key to press, i.e. shift, f1. Defaults to shift key if not provided")
    parser.add_argument('-t', '--time_active', nargs=2, metavar=('START', 'END',),
                        help="If provided, the key will only be pressed during the specified time. i.e -t 8:00 17:00")
    parser.add_argument('-p', '--process', nargs='?',
                        help="Name or regex of running process to trigger the key press.")
    args = parser.parse_args()
    auto_keypress(**vars(args))
