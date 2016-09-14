# encoding: utf-8

import RPi.GPIO as GPIO
import traceback

def start(pin):

    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        # set 14 high, will start watering
        # GPIO.output(pin, True)
        return True
    except Exception as exp:
        traceback.print_exc()
        return False


def stop(pin):

    try:
        GPIO.setmode(GPIO.BCM)
        # GPIO.output(pin, False)
        GPIO.setup(pin, GPIO.IN)
        GPIO.cleanup()
        return True
    except Exception as exp:
        traceback.print_exc()
        return False


def check(pin):
    pass
    try:
        GPIO.setmode(GPIO.BCM)
        status = 'UNKNOWN'
        rtn = GPIO.gpio_function(pin)
        if rtn is GPIO.IN:
            status = 'OFF'
        elif rtn is GPIO.OUT:
            status = 'ON'

        returns = [True, status]
    except Exception as exp:
        traceback.print_exc()
        returns = [False, 'UNKNOWN', exp.message]
    return returns
