#!/usr/bin/python

import time

account = {'id':1001, 'balance':0}

def OpenAccount(acc, amount):
	acc['balance'] = amount

def Withdraw(acc, amount):
	result = 0

	if acc['balance'] - amount > 0:
		result = 1
		time.sleep(1)
		acc['balance'] -= amount

	return result

def CloseAccount(acc):
	del acc

if __name__ == '__main__':

	print "Jack and Jill opened account with id", account['id']
	OpenAccount(account, 10000)
	print "Initial balance = ", account['balance']

	print "Jack withdraw's 7000"
	if Withdraw(account, 7000) == 0:
		print "Jack's withdraw failed"
	print "Jill withdraw's 4000"
	if Withdraw(account, 4000) == 0:
		print "Jill's withdraw failed"

	print "Final balance = ", account['balance']





























