#!/usr/bin/python

import threading
import time

def SenderProc():
	for i in range(1, 6):
		print 'Hello <', i, '> from ', threading.currentThread().getName(), 'on channel', 1001
		time.sleep(1)

def ReceiverProc():
	for i in range(1, 6):
		print 'Received Hello <', i, '> from ', threading.currentThread().getName(), 'on channel', 1001
		time.sleep(1)

if __name__ == '__main__':
	
	threads = [
		threading.Thread(target=SenderProc),
		threading.Thread(target=ReceiverProc),
		threading.Thread(target=SenderProc),
		threading.Thread(target=ReceiverProc),
	]
	
	for t in threads:
		t.start()

	for t in threads:
		t.join()

	print 'Goodbye!'

















