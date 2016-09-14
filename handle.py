import controller
import log


def start(pin):
    log.info('begin starting.')
    rtn = controller.start(pin)
    log.info('finish start')
    return rtn


def check(pin):
    log.info('begin checking.')
    rtn = controller.check(pin)
    log.info('finish check')
    return rtn


def stop(pin):
    log.info('begin stopping.')
    rtn = controller.stop(pin)
    log.info('finish stop')
    return rtn
