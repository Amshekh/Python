#!/usr/bin/python

import threading
import time

"""
text = ''

def GetText():
	global text
	return text

def SetText(value):
	global text
	text = value
"""

slot = threading.local()

def GetText():
	return slot.text

def SetText(value):
	slot.text = value

def PrintCopies(limit):
	i = 1
	while i <= limit:
		print GetText(), 'from', threading.currentThread().getName()
		time.sleep(1)
		i += 1

def ParentProc():
	SetText('Welcome')
	PrintCopies(5)

def ChildProc():
	SetText('Hello')
	PrintCopies(7)


if __name__ == '__main__':
	
	t = threading.Thread(target=ChildProc)
	t.start()

	ParentProc()
	
	t.join()





































