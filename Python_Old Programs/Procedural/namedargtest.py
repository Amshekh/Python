#!/usr/bin/python

def InterestRate(p, n, r=4.5):

	return p * n * r / 100.0

if __name__ == '__main__':

	#print 'Interest rate = ', InterestRate(500000, 5, 4.5)
	print 'Interest rate = ', InterestRate(700000, 7, 5.5)
	print 'Interest rate = ', InterestRate(700000, 7)
	print 'Interest rate = ', InterestRate(n=7, p=700000)

