import socket
import traceback
import handle
import log
import json

__author__ = 'Barry'

# Create a TCP/IP socket
log.info("Start to connecting server.")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# first set 14 pin
pin = 14

# Connect the socket to the port where the server is listening
# server_address = ('45.120.159.147', 8007)
server_address = ('192.168.1.221', 8007)
sock.connect(server_address)

log.info("connect server successful.")

try:
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
            if result[0] is True:
                resp = dict(type=type, status=result[1])
                sock.sendall(json.dumps(resp))
                log.debug('sent resp to server, %s' % json.dumps(resp))
            else:
                resp = dict(type=type, status=result[1], info=result[2])
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




