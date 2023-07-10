#!/usr/bin/python

def Print(ilist):
	for element in ilist:
		print element,
	print '\n'

def PrintIf(ilist, filter):
	for element in ilist:
		if filter(element): print element,
	print '\n'


#****************************************************************************

def Odd(val):

	return val & 1 == 1

if __name__ == '__main__':

	intList = (12, 56, 79, 45, 23)

	print 'All numbers: ',
	Print(intList)

	print 'Odd numbers: ',
	PrintIf(intList, Odd)

	print 'Even numbers: ',
	PrintIf(intList, (lambda val: val & 1 == 0))









