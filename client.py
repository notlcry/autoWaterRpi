import socket
import traceback
import handle
import log
import json
from threading import Thread
import time
import os

__author__ = 'Barry'


def heart_beat(socket_client):
    while True:
        hb_resp = dict(type="HEART_BEAT", result='SUCCESS')
        socket_client.sendall(json.dumps(hb_resp))
        log.debug("Send HeartBeat.")
        time.sleep(30)


# Create a TCP/IP socket
def connect():
    log.info("Start to connecting server.")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('45.120.159.147', 8007)
    # server_address = ('192.168.1.221', 8007)
    sock.connect(server_address)
    log.info("connect server successful.")
    return  sock


def run(sock):
    try:
        log.info('Start Main handle thread.')
        # Send data
        # message = 'I am online.'

        # Look for the response
        while True:
            data = sock.recv(1024)
            log.info('received "%s"' % data)

            if data.__len__() == 0:
                break

            receive = json.loads(data)

            type = receive['type']

            if type == "START":
                log.debug('start...')
                result = handle.start(pin)
                if result is True:
                    resp = dict(type=type, result='SUCCESS')
                    sock.sendall(json.dumps(resp))
                    log.debug('sent resp to server, %s' % json.dumps(resp))
                else:
                    resp = dict(type=type, result='FAIL', info="start relay fail, please check the connection.")
                    sock.sendall(json.dumps(resp))
                    log.debug('sent resp to server, %s' % json.dumps(resp))

            if type == "CHECK":
                results = handle.check(pin)
                log.info(results)
                if results[0] is True:
                    resp = dict(type=type, status=results[1])
                    sock.sendall(json.dumps(resp))
                    log.debug('sent resp to server, %s' % json.dumps(resp))
                else:
                    resp = dict(type=type, status=results[1], info=results[2])
                    sock.sendall(json.dumps(resp))
                    log.debug('sent resp to server, %s' % json.dumps(resp))

            if type == "STOP":
                result = handle.stop(pin)
                if result is True:
                    resp = dict(type=type, result='SUCCESS')
                    sock.sendall(json.dumps(resp))
                    log.debug('sent resp to server, %s' % json.dumps(resp))
                else:
                    resp = dict(type=type, result='FAIL', info="stop relay fail, please check the connection.")
                    sock.sendall(json.dumps(resp))
                    log.debug('sent resp to server, %s' % json.dumps(resp))

    except Exception as exp:
        log.error(exp.message)
        traceback.print_exc()
    finally:
        log.info('closing socket')
        sock.close()
        os._exit(1)

if __name__ == "__main__":
    # first set 14 pin
    pin = 14
    sock = connect()

    # start HB thread
    thread_hb = Thread(target=heart_beat, args=(sock,))
    thread_hb.start()
    # thread_hb.join()

    thread_main = Thread(target=run, args=(sock,))
    thread_main.start()
    # thread_main.join()

