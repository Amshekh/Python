#!/usr/bin/python

intList = (111, 222, 333, 444, 555, 666, 777, 888, 999)
index = 0
item = 0

index = input('Enter index: ')

if index >= 0 and index <= 8:
	item = intList[index]
	print item, 'found at index', index
else:
	print 'Bad index!'

print 'Goodbye'

