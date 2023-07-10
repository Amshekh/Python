#!/usr/bin/python

import sys
from socket import *

if len(sys.argv) < 2:
	print 'USAGE:', sys.argv[0], '<message>'
	exit()

if __name__ == '__main__':

	client = socket(AF_UNIX, SOCK_STREAM)
	client.connect('/tmp/teststrmsock')

	client.send(sys.argv[1])
	response = client.recv(79)

	print 'Response =', response

	client.close()









