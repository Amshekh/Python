#!/usr/bin/python

from threading import Thread

class MyThread(Thread):

	def __init__(self, target):
		Thread.__init__(self, target=target)

	def run(self):
		print "Child-thread's run method executed"

def ThreadProc():	
	print 'Thread procedure'

if __name__ == '__main__':
	
	t = MyThread(ThreadProc)
	t.start()

	















