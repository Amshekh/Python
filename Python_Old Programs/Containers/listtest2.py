#!/usr/bin/python

jack = [1001, 'Jack', 25000]

index = 0

index = input('Enter key: ')

jack.reverse()

if index == 0:
	print jack[0]
elif index == 1:
	print jack[1]
elif index == 2:
	print jack[2]
else:
	print 'Bad index!'


