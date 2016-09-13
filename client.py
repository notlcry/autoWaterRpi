import socket
import sys
import handle
import log

__author__ = 'Barry'

# Create a TCP/IP socket
log.logger.info("Start to connecting server.")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8007)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:

    # Send data
    message = 'I am online.'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    # Look for the response

    while True:
        data = sock.recv(16)
        print >>sys.stderr, 'received "%s"' % data

        if data.__len__() == 0:
            break

        if data == "START":
            handle.start()

        if data == "CHECK":
            result = handle.check()
            if result is True:
                sock.sendall('Status:ON')
            else:
                sock.sendall('Status:OFF')

        if data == "STOP":
            handle.stop()

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()




