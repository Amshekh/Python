#!/usr/bin/python

import threading
import time

evt = threading.Event()

def ThreadProc():
	
	for i in range(1, 11):
		print 'Hello', i, 'from', threading.currentThread().getName()
		time.sleep(1)

	evt.wait()
	print 'Goodbye!'

if __name__ == '__main__':

	t = threading.Thread(target=ThreadProc)
	t.setDaemon(True)
	t.start()

	for i in range(1, 21):
		print 'Welcome', i, 'from', threading.currentThread().getName()
		time.sleep(1)
		
	evt.set()

	t.join()











