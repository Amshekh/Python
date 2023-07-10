#!/usr/bin/python

import threading
import time

account = {'id':1001, 'balance':0, 'lock':0}

def OpenAccount(acc, amount):
	acc['balance'] = amount
	acc['lock'] = threading.Lock()

def Withdraw(acc, amount):
	result = 0

	acc['lock'].acquire()

	if acc['balance'] - amount > 0:
		result = 1
		time.sleep(1)
		acc['balance'] -= amount

	acc['lock'].release()

	return result

def CloseAccount(acc):
	acc['lock'] = 0
	del acc

def ThreadProc(*args):
	acc = args[0]
	amount = args[1]

	print "Jill withdraw's 4000"
	if Withdraw(account, 4000) == 0:
		print "Jill's withdraw failed"

if __name__ == '__main__':

	print "Jack and Jill opened account with id", account['id']
	OpenAccount(account, 10000)
	print "Initial balance = ", account['balance']

	t = threading.Thread(target=ThreadProc, args=(account, 4000))	
	t.start()

	print "Jack withdraw's 7000"
	if Withdraw(account, 7000) == 0:
		print "Jack's withdraw failed"

	print "Final balance = ", account['balance']





























