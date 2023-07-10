#!/usr/bin/python

import threading
import time

def ThreadProc():
	
	for i in range(1, 21):
		print 'Hello', i, 'from', threading.currentThread().getName()
		time.sleep(1)

if __name__ == '__main__':

	t = threading.Thread(target=ThreadProc)
	t.start()

	for i in range(1, 11):
		print 'Welcome', i, 'from', threading.currentThread().getName()
		time.sleep(1)











