#!/usr/bin/python

intList = (111, 222, 333, 444, 555, 666, 777, 888, 999)
index = 0
item = 0

index = input('Enter index: ')

if index < 0 or index > 8:
	print 'Bad index!'
else:
	item = intList[index]
	print item, 'found at index', index

print 'Goodbye'

