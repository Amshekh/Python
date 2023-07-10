#!/usr/bin/python

import threading
import time

def SenderProc(*args):
	limit = args[0]
	msg = args[1]
	channel = args[2]
	for i in range(1, limit):
		print msg, '<', i, '> from ', threading.currentThread().getName(), 'on channel', channel
		time.sleep(1)

def ReceiverProc(*args):
	limit = args[0]
	msg = args[1]
	channel = args[2]
	for i in range(1, limit):
		print 'Received', msg, '<', i, '> from ', threading.currentThread().getName(), 'on channel', channel
		time.sleep(1)

if __name__ == '__main__':
	
	threads = [
		threading.Thread(target=SenderProc, args=(6, 'Hello', 1001)),
		threading.Thread(target=ReceiverProc, args=(6, 'Hello', 1001)),
		threading.Thread(target=SenderProc, args=(8, 'Welcome', 1002)),
		threading.Thread(target=ReceiverProc, args=(8, 'Welcome', 1002))
	]
	
	for t in threads:
		t.start()

	for t in threads:
		t.join()

	print 'Goodbye!'

















