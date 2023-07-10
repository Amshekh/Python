#!/usr/bin/python

import sys

from socket import *

if __name__ == '__main__':

	if len(sys.argv) < 2:
		print 'USAGE:', sys.argv[0], '<message>'
		exit()

	client = socket(AF_UNIX, SOCK_DGRAM)
	status = client.bind('/tmp/testdgrmsock')

	client.sendto(sys.argv[1], '/tmp/testdgrmsock')
	response = client.recv(79)

	print 'Response = ', response

	client.close()

