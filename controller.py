# encoding: utf-8

import RPi.GPIO as GPIO


def start(pin):
    pass

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    # set 14 high, will start watering
    # GPIO.output(pin, True)


def stop(pin):
    pass

    GPIO.setmode(GPIO.BCM)
    # GPIO.output(pin, False)
    GPIO.cleanup()


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

        returns = [True,status]
    except Exception as exp:
        returns = [False, 'UNKNOWN', exp.message]
    return returns
