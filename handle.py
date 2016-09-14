import controller
import log


def start(pin):
    log.info('begin starting.')
    controller.start(pin)


def check(pin):
    log.info('begin checking.')
    controller.check(pin)


def stop(pin):
    log.info('begin stopping.')
    controller.stop(pin)
