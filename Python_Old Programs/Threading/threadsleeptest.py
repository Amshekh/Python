#!/usr/bin/python

import threading
import time

def ThreadProc():
	
	for i in range(1, 11):
		print 'Hello', i, 'from', threading.currentThread().getName()
		time.sleep(1)

	time.sleep(14)
	print 'Goodbye!'

if __name__ == '__main__':

	t = threading.Thread(target=ThreadProc)
	t.setDaemon(True)
	t.start()

	for i in range(1, 21):
		print 'Welcome', i, 'from', threading.currentThread().getName()
		time.sleep(1)
		
	t.join()











