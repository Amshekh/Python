#!/usr/bin/python

intList = (111, 222, 333, 444, 555, 666, 777, 888, 999)
index = 0
item = 0
flag = 0
length = len(intList)

item = input('Enter item: ')

while index < length:
	if item == intList[index]:
		flag = 1
		break
	index += 1

if flag == 1:
	print item, 'found at index', index
else:
	print 'No such item', item







